// C_PUSH constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
@TRUE_0
D;JEQ
@FALSE_0
0;JMP
(TRUE_0)
@SP
A=M-1
M=-1
@CONTINUE_0
0;JMP
(FALSE_0)
@SP
A=M-1
M=0
@CONTINUE_0
0;JMP
(CONTINUE_0)
// C_PUSH constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
@TRUE_1
D;JEQ
@FALSE_1
0;JMP
(TRUE_1)
@SP
A=M-1
M=-1
@CONTINUE_1
0;JMP
(FALSE_1)
@SP
A=M-1
M=0
@CONTINUE_1
0;JMP
(CONTINUE_1)
// C_PUSH constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
@TRUE_2
D;JEQ
@FALSE_2
0;JMP
(TRUE_2)
@SP
A=M-1
M=-1
@CONTINUE_2
0;JMP
(FALSE_2)
@SP
A=M-1
M=0
@CONTINUE_2
0;JMP
(CONTINUE_2)
// C_PUSH constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@TRUE_3
D;JLT
@FALSE_3
0;JMP
(TRUE_3)
@SP
A=M-1
M=-1
@CONTINUE_3
0;JMP
(FALSE_3)
@SP
A=M-1
M=0
@CONTINUE_3
0;JMP
(CONTINUE_3)
// C_PUSH constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@TRUE_4
D;JLT
@FALSE_4
0;JMP
(TRUE_4)
@SP
A=M-1
M=-1
@CONTINUE_4
0;JMP
(FALSE_4)
@SP
A=M-1
M=0
@CONTINUE_4
0;JMP
(CONTINUE_4)
// C_PUSH constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@TRUE_5
D;JLT
@FALSE_5
0;JMP
(TRUE_5)
@SP
A=M-1
M=-1
@CONTINUE_5
0;JMP
(FALSE_5)
@SP
A=M-1
M=0
@CONTINUE_5
0;JMP
(CONTINUE_5)
// C_PUSH constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@TRUE_6
D;JGT
@FALSE_6
0;JMP
(TRUE_6)
@SP
A=M-1
M=-1
@CONTINUE_6
0;JMP
(FALSE_6)
@SP
A=M-1
M=0
@CONTINUE_6
0;JMP
(CONTINUE_6)
// C_PUSH constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@TRUE_7
D;JGT
@FALSE_7
0;JMP
(TRUE_7)
@SP
A=M-1
M=-1
@CONTINUE_7
0;JMP
(FALSE_7)
@SP
A=M-1
M=0
@CONTINUE_7
0;JMP
(CONTINUE_7)
// C_PUSH constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@TRUE_8
D;JGT
@FALSE_8
0;JMP
(TRUE_8)
@SP
A=M-1
M=-1
@CONTINUE_8
0;JMP
(FALSE_8)
@SP
A=M-1
M=0
@CONTINUE_8
0;JMP
(CONTINUE_8)
// C_PUSH constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH constant 53
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
AM=M-1
D=M
A=A-1
M=M+D
// C_PUSH constant 112
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// neg
@SP
A=M-1
M=-M
// and
@SP
AM=M-1
D=M
A=A-1
M=D&M
// C_PUSH constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
// or
@SP
AM=M-1
D=M
A=A-1
M=D|M
// not
@SP
A=M-1
M=!M
