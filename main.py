import os
import sys
import re
import winreg

nonPdfExtensions = []
keywordsToIgnore = ["Card, Deck"]

def main():
    # print(sys.argv)
    if not is_long_path_support_enabled():
        print("Long path support is required please enable")
        return

    directory = sys.argv[1]

    if os.path.isdir(directory):
        directorySearch(directory)
    else:
        # print("Invalid input")
        return 1

    print("Here is the list of unprocessed extensions:")
    for item in nonPdfExtensions:
        print(item)

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

            if name[1] not in nonPdfExtensions:
                nonPdfExtensions.append(name[1])


def processPDF(dirPath, item):
    fregex = r"PZO[0-9A-Z]{3,6}[ -]{0,1}.*"
    if re.match(fregex, item) is None:
        print(item + " is not a paizo pdf name")
        print()
        return

    regex = r"PZO[0-9A-Z]{3,6}"
    # print(re.sub(regex, '', item))
    title_suf = re.sub(regex, '', item).replace(' ', '_')
    dir = dirPath.split("\\")[-1]

    dirsplit = dir.split("-")[0]

    str_list = list(filter(filterFunc, re.split(r'([A-Z][a-z]+)|(PDF)', dirsplit)))

    title_pre = '_'.join(str_list)

    new_title = title_pre + title_suf
    # os.rename((dirPath + "\\" + item).replace("\\", "/"), (dirPath + "\\" + new_title).replace("\\", "/"))
    return


def filterFunc(x):
    if x in ['', "PDF", None]:
        return False
    return True


def is_long_path_support_enabled():
    """
    Checks if long path support is enabled in Windows.

    Returns:
        bool: True if long path support is enabled, False otherwise.
    """
    try:
        key_path = r"SYSTEM\CurrentControlSet\Control\FileSystem"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_READ) as key:
            value, _ = winreg.QueryValueEx(key, "LongPathsEnabled")
            return value == 1
    except FileNotFoundError:
        # The key or value might not exist if long path support is not configured
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


if __name__ == "__main__":
    main()
