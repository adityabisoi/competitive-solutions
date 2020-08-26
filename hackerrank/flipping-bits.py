for _ in range(int(input())):
    var = "{:032b}".format(int(input()))
    s = ''
    for i in var:
        s += '0' if i is '1' else '1'
    print(int(s, 2))
