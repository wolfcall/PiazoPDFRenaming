import os
import sys
import re

def main():
    # print(sys.argv)
    directory = sys.argv[1]

    if os.path.isdir(directory):
        directorySearch(directory)
    else:
        # print("Invalid input")
        return 1

    return 0

def directorySearch(dirPath):
    for itempath in os.listdir(dirPath):
        name = itempath.split(".",1)
        if len(name) == 1:
            # print(f"Directory: {name}")
            directorySearch(f"{dirPath}\\{itempath}")
        elif name[1] == "pdf":
            # print(f"Pdf: {itempath}")
            processPDF(dirPath, itempath)
        else:
            # print(f"Not a pdf: {itempath}")
            return


def processPDF(dirPath, item):
    if re.match(r"PZO[A-Z0-9](5,6) .+", item) is not None:
        return
    print(f"{dirPath}\\{item}")
    return


if __name__ == "__main__":
    main()
