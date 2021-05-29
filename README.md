# Intepretator
A fully working interpreter, which was created by using PLY instrument.

This dialect is downright primitive and it is so like C++ ---there are string, boolean, and integer variables
and no facilities for interactive input. Moreover, you can create some basic programs by using familiar functions like IF-ELSE, DO-UNTIL and etc. You can create a program, where a robot tries to find the exit from the labyrinth. There are diffrent kinds of walls, which a robot can see, define and drill.

Nevertheless, there are a few interesting aspects of this example:

  - It illustrates a fully working interpreter including lexing, parsing,
    and interpretation of instructions.
 
  - The parser shows how to catch and report various kinds of parsing
    errors in a more graceful way.

  - The example both parses files (supplied on command line) and
    interactive input entered line by line.

  - It shows how you might represent parsed information.  In this case,
    each 'MY LANGUAGE' statement is encoded into a Python tuple containing the
    statement type and parameters.  These tuples are then stored in
    a dictionary indexed by program line numbers.

  - Even though it's just 'ROBOT_LANGUAGE', the parser contains more than 80
    rules and 150 parsing states.


The following files are defined:

   robotmain.py         - High level script that controls everything
   
   robotlex.py          - ROBOT tokenizer
   
   robotgrammar.py      - ROBOT parser
   
   robotinter.py        - ROBOT interpreter that runs parsed programs.

In addition, a number of sample ROBOT programs (.bas suffix) are
provided. 

Have fun!
