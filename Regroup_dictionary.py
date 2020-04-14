# Implement a group_by_owners function that:
# Accepts a dictionary containing the file owner name for each file name.
# Returns a dictionary containing a list of file names for each owner name, in any order.


def group_by_owners(files):
    res = {}
    for file, name in files.items():
        if name not in res.keys():
            res[name] = [file]
        else:
            res[name].append(file)
    return res


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))
