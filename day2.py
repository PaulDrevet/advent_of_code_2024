with open('input.txt') as f:
    lines = f.readlines()
    
def test_level(level):
    state = "safe"
    if level[0] < level[1] :
        for i in range(len(level)-1):
            delta = (level[i] - level[i+1])
            if not (-4 < delta < 0):
                
                state = "unsafe"
                break
    if level[0] > level[1] :
        for i in range(len(level)-1):
            delta = (level[i] - level[i+1])

            if not(4 > delta > 0):
                state = "unsafe"
                break
    if level[0] == level[1] :
        state = "unsafe"
        
    return state
    
def main():  
    unsafe = 0      
    for line in lines :
        level = line.replace("\n", "").split(" ")
        level[:] = list(map(int, level))
        state = test_level(level)
        
        if state == "unsafe" :
            for i in range(len(level)-1):
                temp = level.copy()
                temp.pop(i)
                if test_level(temp) == "safe" :
                    state = "safe"
                    break
        print(state)
        if state == "unsafe":
            unsafe += 1

    print(len(lines)-unsafe)
    
main()