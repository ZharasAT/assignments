string1 = "evil"
string2 = "live"

i = 0
x = 0
for i in string1:
    if len(string1) - len(string2) == 0:
        for x in string2:
            if string1(i) == string2(x):
                print(i == x)
            else:
                x += 1
        i += 1
    else:
        print(string1 + "and" + string2 + "are no anagrams")

print(string1 + "and" + string2 + "are anagrams")