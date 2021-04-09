def simple_match(str1,str2):
    place = []
    for letter1 in str1:
        for letter2 in str2:
            if letter2 == letter1:
                print ('match:',letter1,str1.find(letter1))
                place += [str1.find(letter1)] 
            else:
                continue
    print (place)
    if place[0] + 2 == place[1] +1 == place[2]:
        return (place[0])
    else:
        return (-1)


print(simple_match('location', 'cat') == 2)
print(simple_match('soccer', 'cat') == -1)
print(simple_match('category', 'cat') == 0)
print(simple_match('carpet', 'cat') == -1)