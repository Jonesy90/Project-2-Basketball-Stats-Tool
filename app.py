from constants import PLAYERS, TEAMS

panthers_team = []
bandits_team = []
warriors_team = []

experienced_players = []
inexperienced_players = []

# Converts the string value to a Bool value and assigns it to the correct array.
def clean_data():
    for experience in PLAYERS:
        if experience['experience'] == 'YES':
            experience['experience'] = bool(True) # Converting the 'experience' value to a BOOL.
            experience['height'] = int(experience['height'].split(' inches')[0])
            experienced_players.append(experience)
        else:
            experience['experience'] = bool(False)
            experience['height'] = int(experience['height'].split(' inches')[0])
            inexperienced_players.append(experience)


# Balances out the teams so each team has an even number of experienced and inexperienced players.
def balance_teams():
    counter = 0
    number_players = len(PLAYERS) / len(TEAMS) # Should return 6.

    while len(panthers_team) < number_players:
        panthers_team.append(experienced_players[counter])
        panthers_team.append(inexperienced_players[counter])
        counter += 1
        while len(bandits_team) < number_players:
            bandits_team.append(experienced_players[counter])
            bandits_team.append(inexperienced_players[counter])
            counter += 1
            while len(warriors_team) < number_players:
                warriors_team.append(experienced_players[counter])
                warriors_team.append(inexperienced_players[counter])
                counter += 1

# The main menu of the application.
def menu():
    while True:
        try:
            print('''
                \nBASKETBALL TEAM STATS TOOL
                \n---- MENU ----
                \nHere are your choices:
                \r1) Display Team Stats
                \r2) Quit''')
            user_choice = input("\nEnter an Option: ")
            if user_choice in ['1', '2']:
                return user_choice
            else: 
                input('''
                    \rPlease choose one of the options above.
                    \rRange from 1-2.
                    \rPress Enter to start again.''')
        except ValueError:
            user_choice = input('Invalid Entry. Please try again....')

def sub_menu():
    try:
        print('''
            \n1) Panthers
            \r2) Bandits
            \r3) Warriors''')
        sub_choice = input('\nEnter an Option >:  ')
        if sub_choice.upper() in ['1', '2', '3']:
            return sub_choice
    except ValueError:
        sub_choice = input('Invalid Entry. Please try again....')


def average_height(team):
    average_team_height = 0
    for height in team:
        average_team_height = average_team_height + height['height'] / len(team)
    return average_team_height

def experienced(team):
    experienced_players_count = 0
    inexperienced_players_count = 0

    for experience in team:
        if experience['experience'] == True:
            experienced_players_count += 1
        elif experience['experience'] == False:
            inexperienced_players_count += 1
    return experienced_players_count, inexperienced_players_count 


def app():
    clean_data()
    balance_teams()
    users_choice = menu()

    while True:
        if users_choice == '1':
            try:
                sub_choice = sub_menu()
                if sub_choice == '1':

                    # For Loop calculating the average height of the Panther team.
                    panther_team_average_height = average_height(panthers_team)
                    
                    # For Loop over the Panthers Team to which will increase the counter once a experienced player is found.
                    panther_experienced = experienced(panthers_team)[0]
                    panther_inexperienced = experienced(panthers_team)[1]

                    print(f'''
                        \nTeam: Panthers Stats
                        \n---------------------
                        \nTotal Players: {len(panthers_team)}
                        \rTotal Experienced: {panther_experienced}
                        \rTotal Inexperienced: {panther_inexperienced}
                        \rAverage Height: {int(panther_team_average_height)}
                        \nPlayers on Team:
                        \r{panthers_team[0]['name']}, {panthers_team[1]['name']}, {panthers_team[2]['name']}, {panthers_team[3]['name']}, {panthers_team[4]['name']}, {panthers_team[5]['name']}
                        \nGuardians:
                        \r{panthers_team[0]['guardians']}, {panthers_team[1]['guardians']}, {panthers_team[2]['guardians']}, {panthers_team[3]['guardians']}, {panthers_team[4]['guardians']}, {panthers_team[5]['guardians']}''')

                elif sub_choice == '2':

                    # For Loop calculating the average height of the Bandit team.
                    bandit_team_average_height = average_height(panthers_team)
                    
                    # For Loop over the Panthers Team to which will increase the counter once a experienced player is found.
                    bandit_experienced = experienced(bandits_team)[0]
                    bandit_inexperienced = experienced(bandits_team)[1]

                    print(f'''
                        \nTeam: Bandits Stats
                        \n---------------------
                        \nTotal Players: {len(bandits_team)}
                        \rTotal Experienced: {bandit_experienced}
                        \rTotal Inexperienced: {bandit_inexperienced}
                        \rAverage Height: {int(bandit_team_average_height)}
                        \nPlayers on Team:
                        \n{bandits_team[0]['name']}, {bandits_team[1]['name']}, {bandits_team[2]['name']}, {bandits_team[3]['name']}, {bandits_team[4]['name']}, {bandits_team[5]['name']}\n
                        \nGuardians:
                        \r{bandits_team[0]['guardians']}, {bandits_team[1]['guardians']}, {bandits_team[2]['guardians']}, {bandits_team[3]['guardians']}, {bandits_team[4]['guardians']}, {bandits_team[5]['guardians']}''')
                        
                elif sub_choice == '3':

                    # For Loop calculating the average height of the Warrior team.
                    bandit_team_average_height = average_height(panthers_team)
                    
                    # For Loop over the Panthers Team to which will increase the counter once a experienced player is found.
                    warrior_experienced = experienced(bandits_team)[0]
                    warrior_inexperienced = experienced(bandits_team)[1]

                    print(f'''
                        \nTeam: Warrior Stats
                        \n---------------------
                        \nTotal Players: {len(bandits_team)}
                        \rTotal Experienced: {warrior_experienced}
                        \rTotal Inexperienced: {warrior_inexperienced}
                        \rAverage Height: {int(bandit_team_average_height)}
                        \nPlayers on Team:
                        \n{warriors_team[0]['name']}, {warriors_team[1]['name']}, {warriors_team[2]['name']}, {warriors_team[3]['name']}, {warriors_team[4]['name']}, {warriors_team[5]['name']}\n
                        \nGuardians:
                        \r{warriors_team[0]['guardians']}, {warriors_team[1]['guardians']}, {warriors_team[2]['guardians']}, {warriors_team[3]['guardians']}, {warriors_team[4]['guardians']}, {warriors_team[5]['guardians']}''')
                else:
                    sub_choice = input('Error. Press ENTER to retry:  ')
                users_choice = menu()
            except:
                sub_choice = input('INVALID OPTION. ')
        elif users_choice == '2':
            print("\n\nGOODBYE\n\n")
            break



if __name__ =="__main__":
    app()
