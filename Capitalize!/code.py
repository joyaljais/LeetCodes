def solve(s):
    lst=list(s.capitalize())

    r=''

    for x in range(len(lst)):
        if lst[x-1] == ' ':
            if type(lst[x]) == int:
                r+=lst[x]
            else:
                r+=lst[x].upper()
        
        else:
            r+=lst[x]
    
    return r


if __name__ == '__main__':
    

    s = input()

    result = solve(s)

    print(result)
