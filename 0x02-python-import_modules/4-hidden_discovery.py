#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    unordered_names = []
    for names in dir(hidden_4):
        if names[0] != "_":
            unordered_names.append(names)

    ordered_names = sorted(unordered_names)
    for reorder in ordered_names:
        print("{}".format(reorder))
