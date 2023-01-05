import re
def clean_string(s):
    for i in s:
        if i == "#":
            if s.index(i) == 0:
                s = s[s.index(i)+1:]
            elif s.index(i) == len(s)-1:
                s = s[:s.index(i)-1]
            else:
                s = s[:s.index(i)-1]+ s[s.index(i)+1:]
            print(s)
    return s
print(clean_string(''))