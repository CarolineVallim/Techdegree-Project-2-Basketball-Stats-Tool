# Script filename	
# Use the provided data	
from constants import PLAYERS
from constants import TEAMS

# Script execution	

# Proper use of Dunder Main	
# if __name__ == "__main__":
    
# Clean up data	
def clean_data(players):
    for user in players:
        fixed = {}
        fixed['name'] = user['name']
        fixed['guardians'] = user['guardians']
        if user['experience'] == 'YES':
            fixed['experience'] = True
        else:
            fixed['experience'] = False
        fixed['height'] = int(user['height'].split(' ')[0])
        new_players.append(fixed)
    return new_players

# new_players = []
# new_players.append(clean_data(PLAYERS))
new_players = []
clean_data(PLAYERS)

# Avoid altering imported data	

# Team balancing	
# Coloque uma key nome do time para cada dictonary, para que no futuro seja mais fácil separar os times
def balance_teams(new_players):
    num_players_team = int(len(PLAYERS) / len(TEAMS))
    for user in new_players[:6]:
        user.update({'team': 'Panthers'})
    for user in new_players[6:13]:
        user.update({'team': 'Bandits'})
    for user in new_players[13:19]:
        user.update({'team': 'Warriors'})
    return new_players

balance_teams(new_players)
print(new_players)

def panthers_stats(new_players):
    print("""
Team: Panthers Stats
--------------------
Total players: 6

Players on Team:""")
    for users in new_players:
        panthers_names = [user['name'] for players in new_players if a user['team'] == 'Panthers']
        print(panthers_names)

panthers_stats(new_players)

    
# def display():
#    print("""
#BASKETBALL TEAM STATS TOOL

#----MENU----

#A) Display Team Stats
#B) Quit
#          """)
#    first_menu = input("Enter an option:  ")
#    if first_menu.upper() == "A":
#        print("""
#Choose a team:
#A) Panthers
#B) Bandits
#C) Warriors
#              """)
#        choose_team = input("Enter an option:  ")
#        if choose_team.upper() == "A":
#            print(panters_stats)
#        elif choose_team.upper() == 'B':
#            print(bandits_stats)
#        elif choose_team.upper() == 'C':
#            print(warriors_stats)
#    elif first_menu.upper() == "B":
#        quit

        

        



# Create a menu	

# Display Stats
