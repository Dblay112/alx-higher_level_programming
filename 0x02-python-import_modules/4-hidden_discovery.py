#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    gem = dir(hidden_4)
    for name in gem:
        if gem[:2] != "__":
            print(gem)
