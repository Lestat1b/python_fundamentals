# the list of presidents and their terms
presidents=[
    ("George Washington", "1789-1797"),
    ("John Adams", "1797-1801"),
    ("Thomas Jefferson", "1801-1809"),
    ("James Madison", "1809-1817"),
    ("James Monroe", "1817-1825"),
    ("John Quincy Adams", "1825-1829"),
    ("Andrew Jackson", "1829-1837"),
    ("Martin Van Buren", "1837-1841"),
    ("William Henry Harrison", "1841"),
    ("John Tyler", "1841-1845")
    ]

print("Using a For Loop")
for name, term in presidents:
    last_name = name.split()[-1]

    if last_name.startswith("A"):
        print(last_name + " * - " + term)
    else:
        print(last_name + " - " + term)

    print("Using a While Loop")
    i = 0
    while i < len(presidents):
        name, term = presidents[i]
        last_name = name.split()[-1]
        if last_name.startswith("A"):
            print(last_name + " * - " + term)
        else:
            print(last_name + " - " + term)
        i += 1