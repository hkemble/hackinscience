import sys
if len(sys.argv) == 3:
    print(sum(sys.argv[1:2]))
else:
    print("usage: python3 solution.py OP1 OP2")
