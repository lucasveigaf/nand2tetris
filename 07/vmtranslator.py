import sys
import re

COMMANDS = {
    'push': 'C_PUSH',
    'pop': 'C_POP',
    'add': 'C_ARITHMETIC',
    'sub': 'C_ARITHMETIC',
    'neg': 'C_ARITHMETIC',
    'eq': 'C_ARITHMETIC',
    'gt': 'C_ARITHMETIC',
    'lt': 'C_ARITHMETIC',
    'and': 'C_ARITHMETIC',
    'or': 'C_ARITHMETIC',
    'not': 'C_ARITHMETIC',
}
SYMBOLS = {
    'local': 'LCL',
    'argument': 'ARG',
    'this': 'THIS',
    'that': 'THAT'
}
TEMP_BASE = 5
POINTER_BASE = 3

class Parser():
    currentLineNumber = 0
    currentCommand = { 'commandType': None, 'arg1': None, 'arg2': None }

    def __init__(self, fileName):
        f = open(fileName, "r")
        self.lines = []
        lines = f.readlines()
        for line in lines:
            if line.startswith('/') or line.startswith('\n'):
                continue

            self.lines.append(line)

    def hasMoreCommands(self):
        return self.currentLineNumber != len(self.lines)

    def advance(self):
        if self.hasMoreCommands():
            currentLine = self.lines[self.currentLineNumber].replace('\n', '')
            lineArgs = currentLine.split(' ')
            commandType = COMMANDS[lineArgs[0]]
            if commandType == 'C_ARITHMETIC':
                self.currentCommand = {
                    'commandType': commandType,
                    'arg1': lineArgs[0],
                    'arg2': None,
                }
            else:
                self.currentCommand = {
                    'commandType': commandType,
                    'arg1': lineArgs[1] if len(lineArgs) > 1 else None,
                    'arg2': lineArgs[2] if len(lineArgs) > 2 else None,
                }

            self.incrementCounter()
        return

    def commandType(self):
        return self.currentCommand['commandType']

    def arg1(self):
        return self.currentCommand['arg1']

    def arg2(self):
        return self.currentCommand['arg2']

    def incrementCounter(self):
        self.currentLineNumber += 1
        return


class CodeWriter():
    fileName = ''
    jmpCount = 0

    def __init__(self, fileName):
        self.setFileName(fileName)

    def setFileName(self, fileName):
        self.fileName = fileName
        self.outputFile = open(self.fileName, 'w')

    def writeArithmetic(self, command):
        topStackIntoD = [
            '@SP',
            'AM=M-1',
            'D=M',
            'A=A-1',
        ]
        topStackIntoM = [
            '@SP',
            'A=M-1',
        ]
        asmCommands = []

        if command == 'add':
            asmCommands.extend(topStackIntoD)
            asmCommands.append('M=M+D')

        if command == 'sub':
            asmCommands.extend(topStackIntoD)
            asmCommands.append('M=M-D')

        if command == 'neg':
            asmCommands.extend(topStackIntoM)
            asmCommands.append('M=-M')

        if command in ['eq', 'gt', 'lt']:
            asmCommands.extend(topStackIntoD)
            trueLoop = 'TRUE_{}'.format(self.jmpCount)
            falseLoop = 'FALSE_{}'.format(self.jmpCount)
            mainLoop = 'CONTINUE_{}'.format(self.jmpCount)
            asmCommands.extend([
                'D=M-D',
                '@{}'.format(trueLoop),
                'D;J{}'.format(command.upper()),
                '@{}'.format(falseLoop),
                '0;JMP',
                '({})'.format(trueLoop),
                '@SP',
                'A=M-1',
                'M=-1',
                '@{}'.format(mainLoop),
                '0;JMP',
                '({})'.format(falseLoop),
                '@SP',
                'A=M-1',
                'M=0',
                '@{}'.format(mainLoop),
                '0;JMP',
                '({})'.format(mainLoop),
            ])
            self.jmpCount += 1

        if command == 'and':
            asmCommands.extend(topStackIntoD)
            asmCommands.append('M=D&M')

        if command == 'or':
            asmCommands.extend(topStackIntoD)
            asmCommands.append('M=D|M')

        if command == 'not':
            asmCommands.extend(topStackIntoM)
            asmCommands.append('M=!M')

        asmCommands.insert(0, '// {}'.format(command))
        for line in asmCommands:
            self.outputFile.write("%s\n" % line)

    def writePushPop(self, command, segment, index, filename):
        index = int(index)
        dToStack = [
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1',
        ]
        asmCommands = []
        if command == COMMANDS['push']:
            if segment == 'constant':
                asmCommands = [
                    '@{}'.format(str(index)),
                    'D=A',
                ]
                asmCommands.extend(dToStack)

            if segment == 'static':
                asmCommands = [
                    '@{}.{}'.format(filename.replace('.', ''), str(index)),
                    'D=M',
                ]
                asmCommands.extend(dToStack)

            if segment == 'temp':
                asmCommands = [
                    '@{}'.format(str(TEMP_BASE + index)),
                    'D=M',
                ]
                asmCommands.extend(dToStack)

            if segment == 'pointer':
                asmCommands = [
                    '@{}'.format(str(POINTER_BASE + index)),
                    'D=M',
                ]
                asmCommands.extend(dToStack)

            if segment in ['local', 'argument', 'this', 'that']:
                symbol = SYMBOLS.get(segment)
                asmCommands = [
                    '@{}'.format(str(index)),
                    'D=A',
                    '@{}'.format(symbol),
                    'A=M+D',
                    'D=M',
                ]
                asmCommands.extend(dToStack)

        if command == COMMANDS['pop']:
            stackToD = [
                '@SP',
                'AM=M-1',
                'D=M',
                'M=0',
            ]
            if segment == 'static':
                asmCommands.extend(stackToD)
                asmCommands.extend([
                    '@{}.{}'.format(filename.replace('.', ''), str(index)),
                    'M=D'
                ])

            if segment == 'pointer':
                asmCommands.extend(stackToD)
                asmCommands.extend([
                    '@{}'.format(str(POINTER_BASE + index)),
                    'M=D'
                ])

            if segment == 'temp':
                asmCommands.extend(stackToD)
                asmCommands.extend([
                    '@{}'.format(str(TEMP_BASE + index)),
                    'M=D'
                ])

            if segment in ['local', 'argument', 'this', 'that']:
                symbol = SYMBOLS.get(segment)
                asmCommands = [
                    '@{}'.format(str(index)),
                    'D=A',
                    '@{}'.format(symbol),
                    'D=D+M',
                    '@R13',
                    'M=D',
                    '@SP',
                    'AM=M-1',
                    'D=M',
                    'M=0',
                    '@R13',
                    'A=M',
                    'M=D'
                ]
        asmCommands.insert(0, '// {} {} {}'.format(command, segment, index))
        for line in asmCommands:
            self.outputFile.write("%s\n" % line)

    def close(self):
        self.outputFile.close()


if __name__ == '__main__':
    vmFilePath = sys.argv[1]
    parser = Parser(vmFilePath)
    outputFileName = sys.argv[2] if len(sys.argv) > 1 else vmFilePath
    codeWriter = CodeWriter(outputFileName)

    while parser.hasMoreCommands():
        parser.advance()
        commandType = parser.commandType()
        if commandType == 'C_ARITHMETIC':
            command = parser.arg1()
            codeWriter.writeArithmetic(command)

        if commandType == 'C_PUSH' or commandType == 'C_POP':
            segment = parser.arg1()
            index = parser.arg2()
            vmFileName = vmFilePath.split('/')[-1]
            codeWriter.writePushPop(commandType, segment, index, vmFileName)
    
    codeWriter.close()
