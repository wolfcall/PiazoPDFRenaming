import os
import sys
import re

def main():
    print(sys.argv)
    directory = sys.argv[1]

    for item in os.listdir(directory):
        name = item.split(".", 1)

        print(name)
        if len(name) == 1:
            print(f"Directory: {name}")
        elif name[1] == "pdf":
            print(f"Pdf in root: {item}")
        else:
            print(f"Not a pdf: {item}")

    return 0



if __name__ == "__main__":
    main()
