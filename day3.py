import re

with open('input.txt') as f:
    lines = f.readlines()

s = ''.join(lines)
matches = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", s)

correctMatches = []
ok = True
for i in range(len(matches)):
    print(matches[i])
    if matches[i]  == "don't()":
        ok = False
    elif matches[i] == "do()" :
        ok = True
    elif ok :
        correctMatches.append(matches[i])
        
res = 0

for match in correctMatches :
    x1, x2 = match.replace("mul(","").replace(")","").split(",")
    res += int(x1) * int(x2)

print(res)
    
    
