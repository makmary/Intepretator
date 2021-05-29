import sys
import robotlex
import robotgrammar
import robotinter

data = open("robot_go.bas").read()
print(data)
prog = robotgrammar.parse(data)
print(prog)
if not prog:
    raise SystemExit
b = robotinter.MyInterpreter(prog)
keys = list(prog)
if keys[0] > 0:
    b.add_statements(prog)
try:
    b.run()
    raise SystemExit
except RuntimeError:
    pass


