#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arglen = 0
    for i in range(len(sys.argv) - 1):
        arglen += int(sys.argv[i + 1])
    print("{}".format(arglen))
