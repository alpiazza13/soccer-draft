# sites for getting player info
# https://fantasy.premierleague.com/statistics
# https://www.premierleague.com/players?se=274&cl=-1

# To do:
# Tell user how many picks left
# Show user other people’s teams
# Maybe allow only first/last name to work?
# Make lower/upper case irrelevant
# make it so user can ask what position a specific player is - if he asks that, tell him to type the player, then check which list it's in

from helpers import is_similar

def draft(gks, defs, mids, fwds, users, rounds):
    all_players = gks + defs + mids + fwds
    picked_players = []
    number_of_users = len(users)
    #create a list with one empty list for each user
    user_teams = [[] for i in range(number_of_users)]
    for i in range(rounds):
        j = 0
        #each user picks once per round
        while j < number_of_users:
            this_user = users[j]
            this_team = user_teams[j]
            print("It's ", this_user, "'s turn.")
            commands = ["My players", "My gks", "My defs", "My mids", "My fwds", "Remaining players", "Remaining gks", "Remaining defs", "Remaining mids", "Remainig fwds"]
            print("Available commands:")
            print(", ".join(commands))
            user_input = input("Either pick a player or choose from the above commands.\n")
            if user_input == "Remaining players":
                print("\n".join(all_players))
            elif user_input == "My players":
                print(", ".join(this_team))
            elif user_input == "Remaining gks":
                remaining = [gk for gk in gks if gk not in picked_players]
                print("\n".join(remaining))
            elif user_input == "Remaining defs":
                remaining = [defender for defender in defs if defender not in picked_players]
                print("\n".join(remaining))
            elif user_input == "Remaining mids":
                remaining = [mid for mid in mids if mid not in picked_players]
                print("\n".join(remaining))
            elif user_input == "Remaining fwds":
                remaining = [fwd for fwd in fwds if fwd not in picked_players]
                print("\n".join(remaining))
            elif user_input == "My gks":
                your = [player for player in this_team if player in gks]
                print(", ".join(your))
            elif user_input == "My defs":
                your = [player for player in this_team if player in defs]
                print(", ".join(your))
            elif user_input == "My mids":
                your = [player for player in this_team if player in mids]
                print(", ".join(your))
            elif user_input == "My fwds":
                your = [player for player in this_team if player in fwds]
                print(", ".join(your))
            elif user_input in picked_players:
                print("Player already picked - try again!")
            elif user_input not in all_players:
                print("Not a real player (or invalid request) - try again!")
                suggestions = [player for player in all_players if is_similar(player, user_input)]
                if suggestions != []:
                    print("Did you mean?")
                    print(", ".join(suggestions))
            else:
                print("You - ", this_user, " - picked ", user_input)
                this_team.append(user_input)
                picked_players.append(user_input)
                all_players.remove(user_input)
                j += 1

    for i in range(number_of_users):
        # print("Team", users[i],":", user_teams[i])
        this_team = user_teams[i]
        your_gks = [player for player in this_team if player in gks]
        your_defs = [player for player in this_team if player in defs]
        your_mids = [player for player in this_team if player in mids]
        your_fwds = [player for player in this_team if player in fwds]
        print("Team", users[i],":")
        print(" - ".join(your_gks))
        print(" - ".join(your_defs))
        print(" - ".join(your_mids))
        print(" - ".join(your_fwds))



chelsea_gks = ["Kepa", "Cech", "Courtois", "Caballero"]
chelsea_defs = ["Zouma", "Rudiger", "Azpilicueta", "James", "Christensen",
           "Terry", "Cahill", "Cole", "Alonso", "Tomori", "Ampadu",
           "Lamptey", "Ake", "Luiz", "Bertrand", "Kennedy", "Ivanovic"]
chelsea_mids = ["Kante", "Fabregas", "Jorginho", "Kovacic", "Mount",
           "Lampard", "Essein", "Oscar", "Ramires", "Loftus-Cheek",
           "Meireles", "Matic", "Mata", "Makelele", "Gilmour"]
chelsea_fwds = ["Drogba", "Costa", "Lukaku", "Morata", "Torres",
            "Hazard", "Willian", "Pedro", "Pulisic", "Hudson-Odoi", "Zola", "Robben"]

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

# Goalies don't include Dean Henderson for some reason, fwds don't include Harry Kane
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


still_playing = True
while still_playing == True:

    users = []
    inp = input("How many teams will paricipate in this draft? ")
    # maybe check for error here
    number = int(inp)
    for i in range(number):
        #fix this to put i in
        team = input("Enter team name: ")
        users.append(team)

    inp = input("How many players per team would you like? ")
    # maybe check for error here
    per_team = int(inp)

    z = 0
    while z < 1:
        inp = input("Would you like to draft from Chelsea players or all premier league players?\n Type: Chelsea or All  ")
        if inp == "All":
            draft(goalies, defenders, midfielders, forwards, users, per_team)
            print("PL draft starting now!")
            z+=1
        elif inp == "Chelsea":
            print("Chelsea draft starting now!")
            draft(chelsea_gks, chelsea_defs, chelsea_mids, chelsea_fwds, users, per_team)
            z+=1
        else:
            print("Make sure you spelled it right")
    inp = input("Would you like to draft again? Yes or No?  ")
    if inp == "No":
        still_playing = False
