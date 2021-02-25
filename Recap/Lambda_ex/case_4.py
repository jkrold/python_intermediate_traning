from random import uniform

random_num_lst = [int(uniform(0,101)) for i in range(0,9)]
print(random_num_lst)

print(list(map(lambda number: number*2, random_num_lst)))

