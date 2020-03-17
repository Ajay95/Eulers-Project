str1="aabbbbcccccddddaaaaaaaaa"
str2='abcd'


def string_short(string1):
    count=1
    x=[]
    for index,i in enumerate(string1):
        print(i)
        try:
            if i == string1[index+1]:
                count=count+1
            else:
                print(count)
                x.append(i)
                x.append(str(count))
                count=1
        except:
                x.append(i)
                x.append(str(count))
    return x
        
    
print("".join(string_short(str2)))