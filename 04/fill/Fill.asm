// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// color = 0
// screenaddr = SCREEN
// i = 0
// limit = 8192

// LOOP_PRINT_SCREEN:
//   if i > limit goto RESET
//   color = 1
//   r[screenaddr] = -1
//   screenaddr = screenaddr - 1
//   goto LOOP_PRINT_SCREEN

// RESET:
//   color = 0
//   screenaddr = SCREEN
//   i = 0
//   goto LOOP_KB

// LOOP_KB:
//   if @KBD > 0 goto LOOP_PRINT_SCREEN

  // @SCREEN
  // D=A
  // @screenaddr
  // M=D // screenaddr == SCREEN
  // @color
  // M=0 // color == 0
  // @8192
  // D=A
  // @i
  // M=D // i == 8192

// (LOOP_KB)
//   @KBD
//   D=M
//   @LOOP_PRINT_SCREEN
//   D;JGT
//   @LOOP_KB
//   0;JMP

  @RESET
  0;JMP

(SET_WHITE)
  @color
  M=0
  @LOOP_PRINT_SCREEN
  0;JMP

(SET_BLACK)
  @color
  M=-1
  @LOOP_PRINT_SCREEN
  0;JMP

(LOOP_PRINT_SCREEN)
  @i
  D=M
  @limit
  D=D-M
  @RESET
  D;JEQ
  @color
  D=M
  @screenaddr
  A=M
  M=D // sets bit to the selected color
  @i
  M=M+1
  @screenaddr
  M=M+1
  @LOOP_PRINT_SCREEN
  0;JMP

(RESET)
  @SCREEN
  D=A
  @screenaddr
  M=D // screenaddr == SCREEN
  @8192
  D=A
  @limit
  M=D // i == 8192
  @i
  M=1
  // reads KBD and sets the correct color to fill screen and starts screen loop again
  @KBD
  D=M
  @SET_BLACK
  D;JGT
  @SET_WHITE
  D;JEQ
