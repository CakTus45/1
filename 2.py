# def strcounter(s):
#     adict = {}
#     for i in s:
#         adict[i] = adict.get(i, 0) + 1
#     for j in adict:
#         print(j, adict[j])
# a

# def strcounter(s):
#     for i in s:
#         counter = 0
#         for j in s:
#             if i==j:
#                 counter += 1
#         print(i, counter)


def strcounter(s):
    for i in set(s):
        counter = 0
        for j in s:
            if i==j:
                counter += 1
        print(i, counter)
strcounter("wwwaaaaa")
