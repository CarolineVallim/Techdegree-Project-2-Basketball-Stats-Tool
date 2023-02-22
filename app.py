
from constants import PLAYERS
from constants import TEAMS
import random


def clean_data(players):
    for user in players:
        fixed = {}
        fixed['name'] = user['name']
        fixed['guardians'] = user['guardians'].split(' and ')
        if user['experience'] == 'YES':
            fixed['experience'] = True
        else:
            fixed['experience'] = False
        fixed['height'] = int(user['height'].split(' ')[0])
        clean_data_players.append(fixed)
    return clean_data_players


def balance_teams():
    player_exp = [user for user in clean_data_players if user['experience'] == True]
    player_no_exp = [user for user in clean_data_players if user['experience'] == False]
    
    random.shuffle(player_exp)
    random.shuffle(player_no_exp)
    
    for x in range(len(TEAMS)):
        team = []
        for i in range(num_player_team // 2):
            team.append(player_exp.pop())
            team.append(player_no_exp.pop())
            
        for dict in team:
            dict.update({'team': TEAMS[x]})
            
        distribute_team.extend(team)


def stats(option_selected):
    name = []
    guardians = []
    name_str = ''
    total_experienced = 0
    total_inexperienced = 0
    sum_height = 0
    average = 0
    
    for user in distribute_team:
        if user['team'] == option_selected:
            name.append(user['name'])
            name_str = ', '.join(name)
    
    for user in distribute_team:
        if user['team'] == option_selected:
            guardians.extend(user['guardians'])
            guardians_str = ', '.join(guardians)
    
    for user in distribute_team:
        if user['team'] == option_selected and user['experience'] == True:
            total_experienced += 1
    
    for user in distribute_team:
        if user['team'] == option_selected and user['experience'] == False:
            total_inexperienced += 1
    
    for user in distribute_team:
        if user['team'] == option_selected:
            sum_height += user['height']
    
    average = sum_height / num_player_team
    
    print('\nTeam: {} Stats'.format(option_selected))
    print('-' * 30)
    print('\nTotal players: ',(num_player_team))
    print('Total experienced: ',(total_experienced))
    print('Total inexperienced: ',(total_inexperienced))
    print('Average height: {:.2f}'.format(average))
    print('\nPlayers on Team:')
    print(name_str)
    print('\nGuardians:')
    print(guardians_str)


def validation():
    try:
        select_team = int(input("Enter an option:  "))
        if select_team == 1:
            stats('Panthers')
            continue_stats()
        elif select_team == 2:
            stats('Bandits')
            continue_stats()
        elif select_team == 3:
            stats('Warriors')
            continue_stats()
        else:
            print('You need to select an option. Only 1, 2 or 3.')
            return validation()
    except ValueError as err:
        print('You need to select a number. It can be 1, 2 or 3. Try again.')
        return validation()


def continue_stats():
    answer = str(input('\nDo you want to continue?  Y/N  '))
    if answer.upper() == 'Y':
        display()
    elif answer.upper() == 'N':
        quit
    else:
        print('You need to type only Y for continue and N for quit')
        return continue_stats()


def display():
    print("""
BASKETBALL TEAM STATS TOOL

----MENU----

A) Display Team Stats
B) Quit
          """)
    first_menu = input('Enter an option: A/B  ')
    if first_menu.upper() == 'A':
        print("""
Choose a team:
1) Panthers
2) Bandits
3) Warriors
              """)
        
        validation()
        
    elif first_menu.upper() == 'B':
        print('...')
    else:
        print('This option is not available. You need to type only A or B.')
        return display()


if __name__ == "__main__":
    clean_data_players = []

    clean_data(PLAYERS)

    distribute_team = []

    num_player_team = int(len(PLAYERS) / len(TEAMS))

    balance_teams()

    display()