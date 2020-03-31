x = gets
puts x.size

def draft(gks, defs, mids, fwds, users)
    #picked players will be removed so remaining players can be viewed
    all_players = gks + defs + mids + fwds
    picked_players = []
    number_of_users = users.size
    #create a list with one empty list for each user
    user_teams = []
    for i in 1..number_of_users do
        user_teams << []
    end

    for i in 1..3 do
        j = 0
        while j < number_of_users
            puts "It's #{users[j]}'s turn. Pick a player or something."
            user_input = gets.chomp
            if user_input == "Remaining players"
                puts all_players
            elsif user_input == "My players"
                puts user_teams[j]
            elsif picked_players.include? user_input
                puts "Player already picked - try again!"
            elsif not all_players.include? user_input
                puts "Not a real player (or invalid request) - try again!"
            else
                puts "#{users[j]} picked #{user_input}"
                user_teams[j] << user_input
                picked_players << user_input
                all_players.delete(user_input)
                j += 1
            end
        end
    end

    for i in 0..number_of_users-1 do
        puts "#{users[i]}: #{user_teams[i]}"
    end

end


gks_ex = ["Kepa", "Casillas", "Hart"]
defs_ex = ["Zouma", "Rudiger", "Azpilicueta", "James", "Christensen",
           "Terry", "Cahill", "Cole", "Alonso", "Tomori",
           "Lamptey", "Ake", "Luiz", "Bertrand", "Kennedy"]
mids_ex = ["Kante", "Fabregas", "Jorginho", "Kovacic", "Mount",
           "Lampard", "Essein", "Oscar", "Ramires", "Loftus-Cheek",
           "Meireles", "Matic", "Mata", "Makelele", "Gilmour"]
fwds_ex = ["Drogba", "Costa", "Lukaku", "Morata", "Torres",
            "Hazard", "Willian", "Pedro", "Pulisic", "Hudson-Odoi"]
users_ex = ["Alex", "Kevin"]

draft(gks_ex, defs_ex, mids_ex, fwds_ex, users_ex)
