lst = ["Adam", "Zeke", "Philip", "Anna", "Robert", "Elisabeth", "Dorothy", "Wiliam", "Tom"]

growing_length_lst = sorted(lst, key=lambda name: len(name))
print(growing_length_lst)

descending_length_lst = sorted(lst, key=lambda name: len(name), reverse=True)
print(descending_length_lst)

lst_by_first_letter = sorted(lst, key=lambda name: name[0])
print(lst_by_first_letter)

