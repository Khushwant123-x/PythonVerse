def rprint(lst):
    if not lst:
        return
    print(lst[-1],end=' ')

    rprint(lst[:-1])

lst=[1,2,3,4]
rprint(lst)