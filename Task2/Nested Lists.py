li = []
ls = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    li.append([name, score])
    ls.append(score)
#li being sorted by name    
li.sort(key= lambda x: x[0])

# sorting scores to find the second to lowest
s = set(ls)
s = sorted(s)
# lowest == s[0], so s[1] is the second lowest grade

for name, score in li:
    if score == s[1]:
        print(name)
