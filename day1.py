with open('input.txt') as f:
    lines = f.readlines()
    
    l1 = []
    l2 = []
for line in lines :
    line = line.replace('\n','')
    l1.append(line.split(' ')[0])
    l2.append(line.split(' ')[len(line.split(' '))-1])

l1.sort()
l2.sort()

s = 0

# for i in range(len(l1)):
#     s += abs(int(l1[i])-int(l2[i]))

for x in l1:
    s += int(x) * l2.count(x)
    
print(s)