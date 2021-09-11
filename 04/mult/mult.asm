// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// product = 0
// multiplicand = R0
// multiplier = R1

// LOOP:
//   if multiplier < 1 goto END
//   product = product + multiplicand
//   multiplier = multiplier - 1
//   goto LOOP

// END:
//   R2 = product


  @R0
  D=M
  @multiplicand
  M=D // multiplicand == R0
  @R1
  D=M
  @multiplier
  M=D // multiplicand == R1
  @product
  M=0 // product == 0
  
(LOOP)
  @multiplier
  D=M
  @STOP
  D;JEQ

  @multiplicand
  D=M
  @product
  M=D+M
  @multiplier
  M=M-1
  @LOOP
  0;JMP


(STOP)
  @product
  D=M
  @R2
  M=D
  @END
  0;JMP

(END)
  @END
  0;JMP