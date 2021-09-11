import sys
import re


class SymbolTable():
    variableCounter = 16
    symbols = {
        'SP': '0',
        'LCL': '1',
        'ARG': '2',
        'THIS': '3',
        'THAT': '4',
        'R0': '0',
        'R1': '1',
        'R2': '2',
        'R3': '3',
        'R4': '4',
        'R5': '5',
        'R6': '6',
        'R7': '7',
        'R8': '8',
        'R9': '9',
        'R10': '10',
        'R11': '11',
        'R12': '12',
        'R13': '13',
        'R14': '14',
        'R15': '15',
        'SCREEN': '16384',
        'KBD': '24576',
    }

    def has(self, symbol):
        return symbol in self.symbols

    def set(self, symbol, addr):
        self.symbols[symbol] = addr

    def get(self):
        return self.symbols

    def getOrSet(self, symbol):
        if symbol in self.symbols:
            return self.symbols[symbol]

        addr = str(self.variableCounter)
        self.symbols[symbol] = addr
        self.variableCounter += 1
        return addr


class Parser():
    lineCounter = 0
    realCount = 0

    def __init__(self, fileName):
        f = open(fileName, "r")
        self.lines = f.readlines()
        self.symbolTable = SymbolTable()
        self.resolveLabels()

    def resolveLabels(self):
        i = 0
        for line in self.lines:
            cleanLine = self.cleanLine(line)
            if cleanLine == '':
                continue

            if cleanLine.startswith('('):
                value = cleanLine.replace('(', '').replace(')', '')
                if not self.symbolTable.has(value):
                    self.symbolTable.set(value, i)
                    continue
            
            i += 1

        self.lineCounter = 0
        self.realCount = 0


    def hasNext(self):
        return self.lineCounter < len(self.lines) - 1

    def incrementCounter(self):
        self.realCount += 1

    def cleanLine(self, line):
        return line.partition('/')[0].strip().replace('\n', '')

    def getJmp(self, inst):
        return inst.split(';')[1] if ';' in inst else None

    def getDest(self, inst):
        return inst.split('=')[0] if '=' in inst else None

    def getComp(self, inst):
        if '=' in inst and ';' in inst:
            dest, comp, *jump = re.split(r'[=;]+', cleanLine)
            return comp

        if '=' in inst:
            return inst.split('=')[1]

        return inst.split(';')[0]

    def getNext(self):
        self.lineCounter += 1
        line = self.lines[self.lineCounter]
        cleanLine = self.cleanLine(line)
        if cleanLine == '':
            return {'isValid': False, 'type': 'invalid'}
        
        if cleanLine.startswith('('):
            return { 'isValid': False, 'type': 'label', 'value': cleanLine }

        instType = 'a' if cleanLine[0] == '@' else 'c'
        baseObj = {'isValid': True, 'contents': cleanLine,
                   'lineNumber': self.realCount, 'type': instType}

        if instType == 'c':
            baseObj['dest'] = self.getDest(cleanLine)
            baseObj['comp'] = self.getComp(cleanLine)
            baseObj['jump'] = self.getJmp(cleanLine)
        else:
            dest = cleanLine[1:]
            if not dest.isdigit():
                dest = self.symbolTable.getOrSet(dest)

            baseObj['dest'] = dest

        self.incrementCounter()
        return baseObj


class Code():
    compTable = {
        '0': '0101010',
        '1': '0111111',
        '-1': '0111010',
        'D': '0001100',
        'A': '0110000',
        '!D': '0001101',
        '!A': '0110001',
        '-D': '0001111',
        '-A': '0110011',
        'D+1': '0011111',
        'A+1': '0110111',
        'D-1': '0001110',
        'A-1': '0110010',
        'D+A': '0000010',
        'D-A': '0010011',
        'A-D': '0000111',
        'D&A': '0000000',
        'D|A': '0010101',
        'M': '1110000',
        '!M': '1110001',
        '-M': '1110011',
        'M+1': '1110111',
        'M-1': '1110010',
        'D+M': '1000010',
        'D-M': '1010011',
        'M-D': '1000111',
        'D&M': '1000000',
        'D|M': '1010101',
    }

    jumpTable = {
        'JGT': '001',
        'JEQ': '010',
        'JGE': '011',
        'JLT': '100',
        'JNE': '101',
        'JLE': '110',
        'JMP': '111',
    }

    def translate(self, code):
        if code['type'] == 'a':
            return self.translateAInst(code)
        return self.translateCInst(code)

    def translateAInst(self, code):
        dest = int(code['dest'])
        binaryDest = f'{dest:015b}'
        destWithOp = '0' + binaryDest
        return destWithOp

    def getDest(self, destInst):
        if not destInst:
            return '000'

        base = list('000')
        if 'A' in destInst:
            base[0] = '1'

        if 'D' in destInst:
            base[1] = '1'

        if 'M' in destInst:
            base[2] = '1'

        return ''.join(base)

    def getJmp(self, destInst):
        return self.jumpTable[destInst] if destInst else '000'

    def translateCInst(self, code):
        comp = self.compTable[code['comp']]
        dest = self.getDest(code['dest'])
        jmp = self.getJmp(code['jump'])
        destWithOp = '111' + comp + dest + jmp
        return destWithOp


class Assembler():
    result = []

    def __init__(self, fileName):
        parser = Parser(fileName)
        while parser.hasNext():
            instruction = parser.getNext()
            if not instruction['isValid']:
                continue

            machineCode = Code().translate(instruction)
            self.result.append(machineCode)

    def getResult(self):
        return self.result


if __name__ == '__main__':
    asmFile = sys.argv[1]
    assembler = Assembler(asmFile)
    result = assembler.getResult()

    with open(sys.argv[2], 'w') as f:
        for line in result:
            f.write("%s\n" % line)
