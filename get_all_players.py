file = open("all_players.txt")
names = []
positions = []
i = 1
for line in file:
    if i%2== 1:
        without_photo1 = line[10:]
        without_photo = without_photo1[:-1]
        name_length = len(without_photo) // 2
        name = without_photo[:name_length]
        names.append(name)
    else:
        first_space = line.find(" ")
        position = line[:first_space]
        positions.append(position[:-1])
    i += 1
file.close()

positions[406] += "r"
positions[419] += "r"

for p in positions:
    if p != "Defender" and p!="Forward" and p!="Midfielder" and p!="Goalkeeper":
        print("BAD!!!")


goalies, defenders, midfielders, forwards = [], [], [], []
for i in range(len(positions)):
    position = positions[i]
    name = names[i]
    if position == "Goalkeeper":
        goalies.append(name)
    elif position == "Defender":
        defenders.append(name)
    elif position == "Midfielder":
        midfielders.append(name)
    else:
        forwards.append(name)

# print(goalies)
# print(defenders)
# print(midfielders)
# print(forwards)

number_of_players = len(goalies) + len(defenders) + len(midfielders) + len(forwards)
all_good = number_of_players == len(positions) == len(names)
print(all_good)




# #get goalies (only last names)
# file = open("goalies.txt")
# i = 0
# goalies = []
# for line in file:
#     if i % 6 == 1:
#         goalies.append(line)
#     i+=1
# file.close()
# goalies = [goalie[:-1] for goalie in goalies]
#
# #get defenders (only last names)
# file = open("defenders.txt")
# i = 0
# defenders = []
# for line in file:
#     if i % 6 == 1:
#         defenders.append(line)
#     i+=1
# file.close()
# defenders = [defender[:-1] for defender in defenders]

# def get_duplicates(lst):
#     i = 0
#     dups =[]
#     while i < len(lst):
#         j = i + 1
#         while j < len(lst):
#             if lst[i] == lst[j]:
#                 dups.append(lst[i])
#             j += 1
#         i += 1
#     print(dups)
