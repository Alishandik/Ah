my_dict={"Ali": 2001, "Anya": 2000}
print(my_dict)
print(my_dict.get("Ali"))
print(my_dict.get("Sasha"))
my_dict["Eve"] = 1995
my_dict["Frank"] = 1980
print(my_dict)
del my_dict["Anya"]
print(my_dict)

#множества
my_set = {1, 'apple', 3.14, 'apple', True}
print(my_set)
my_set.add('banana')
my_set.add(False)
my_set.remove(1)
print(my_set)