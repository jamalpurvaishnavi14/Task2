num_A = int(input())
set_A = set(map(int, input().split()))
num_O = int(input())

set_dict = {}

for i in range(num_O):
    query = input()
    elements = set(map(int, input().split()))
    set_dict[query] = elements
    
for k, v in set_dict.items():
        command, len_set = k.split()
        len_set = int(len_set)
        
        if command == 'intersection_update':
            set_A.intersection_update(v)
        
        elif command == 'update':
            set_A.update(v)
        
        elif command == 'symmetric_difference_update':
            set_A.symmetric_difference_update(v)
        
        elif command == 'difference_update':
            set_A.difference_update(v)

print(sum(set_A))
