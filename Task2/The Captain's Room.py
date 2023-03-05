input()
seen_once, seen_again = set(), set()
for element in input().split():
    (seen_again if element in seen_once else seen_once).add(element)
print((seen_once - seen_again).pop())
