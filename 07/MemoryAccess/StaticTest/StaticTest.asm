// C_PUSH constant 111
@111
D=A
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH constant 333
@333
D=A
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH constant 888
@888
D=A
@SP
A=M
M=D
@SP
M=M+1
// C_POP static 8
@SP
AM=M-1
D=M
M=0
@StaticTestvm.8
M=D
// C_POP static 3
@SP
AM=M-1
D=M
M=0
@StaticTestvm.3
M=D
// C_POP static 1
@SP
AM=M-1
D=M
M=0
@StaticTestvm.1
M=D
// C_PUSH static 3
@StaticTestvm.3
D=M
@SP
A=M
M=D
@SP
M=M+1
// C_PUSH static 1
@StaticTestvm.1
D=M
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
// C_PUSH static 8
@StaticTestvm.8
D=M
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
