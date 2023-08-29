#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arglen = len(sys.argv) - 1
    if arglen == 0:
        print("0 arguments.")
    elif arglen == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arglen))
    for i in range(arglen):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
