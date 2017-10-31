le = str(input())
while le.find('@') != -1:
    le = le[:le.find('@')] + le[le.find('@') + 1:]
else:
    print(le)
