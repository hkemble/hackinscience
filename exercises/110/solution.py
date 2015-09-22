import sys
import operator
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul,
       "/": operator.truediv, "%": operator.mod, "^": operator.pow}


def is_int(s):
    try:
        int(s)
        return False
    except ValueError:
        return True


if len(sys.argv) != 4:
    print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")
elif is_int(sys.argv[1]) or int(sys.argv[1]) == 0:
    print("input error")
elif is_int(sys.argv[3]) or int(sys.argv[3]) == 0:
    print("input error")
elif sys.argv[2] not in '+-*/%^' or len(sys.argv[2]) != 1:
    print("input error")
else:
    print(ops[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3])))
