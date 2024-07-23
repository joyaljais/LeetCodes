def count_substring(string, sub_string):
    start=0
    count=0
        
    while(start<=len(string) - len(sub_string)):
        pos=string.find(sub_string,start)
        if pos!=-1:
            count=count+1
            start=pos+1
        else:
            break

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)