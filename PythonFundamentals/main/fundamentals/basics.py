# # methods: def get_methods()
# # classes: MyClassTwo
# # file names: name_file.txt
#
# #
# # x = 3
# # x *= 2 # x = x + 2
# # print(x)
#
# # %
#
# # total_sweets = 100
# # number_of_spartans = 15
# #
# # left_over_sweets = total_sweets % number_of_spartans
# # x =1
#
# trainers = ["Nish", "Cathy", "Paula"]
# nums = [1,2,3,4,5]
# diff_types = [1, "one", 2, "two"]
# nish = trainers[0]
# paula = trainers[-1]
# print(trainers.index("Cathy"))
#
# print(len(nums))
#
# # trainers.append("Phil")
# # last_trainer = trainers.pop(1)
# # trainers.insert(0,"Dean")
# # trainers.remove("Nish")
#
# subset_trainers = trainers[0:2]
# print(subset_trainers)
#
#
# new_trainers = ["Fraz", "Hiyab"]
# trainers.extend(new_trainers)
# print(trainers.__len__())


def print_names(*names):
  for name in names:
    print(name)

print_names("Nish", "Cathy", "Paula")