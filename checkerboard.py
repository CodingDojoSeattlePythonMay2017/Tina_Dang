for i in range(8):
    str_builder = ""
    if i%2 is not 0:
        str_builder += " "
    for j in range (5):
        str_builder += '* '
    print str_builder
