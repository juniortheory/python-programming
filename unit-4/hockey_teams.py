#enter choices for user input
#nhl_website = requests.get('https://www.nhl.com/info/teams')
class HockeyTeam:
    def __init__(self, name, division, conference):
        self.name = name
        self.division = division
        self.conference = conference
        self.roster = []
       
    def add_player(self, player):
        #self.roster.append(player)
        pass
       

    def remove_player(self, player_name):
        #self.player_name.pop()
        pass
       

    def get_roster(self):
        #for team in self.HockeyTeam:
           # print()
        pass

def print_menu():
    print("1. Create hockey team")
    print("2. Add player to a team roster")
    print("3. Remove player from a team roster")
    print("4. Show team roster")

def main():
    hockey_teams = []
    while True:
        print_menu()
        choice = input('Choose your Option: ')
        if choice == '1':
            name, division, conference = input('Enter team name, division and conference(seperated by commas): ').split(',')
            team = HockeyTeam(name, division, conference)
            hockey_teams.append(team)
            print(hockey_teams)
        elif choice == '2':
            name, position, number = input('Enter Player Name, position, number (comma separated)').split(',')
            player = {}
            player['player_name'] = name
            player['position'] = position
            player['shirt_number'] = number
            team_name = input('Enter name of Team to add your player to: ')
            for idx, team in enumerate(hockey_teams):
                if team['name'] == team_name:
                    hockey_teams[idx].roster.append(player)
            else:
                print('team does not exist')
        elif choice == '3':
            name, position, number = input('Enter Player Name, position and number of player you would like to remove: ').split(',')
            player = {}
            player['player_name'] = name
            player['position'] = position
            player['shirt_number'] = number
            team_name = input('Enter name of Team you would like to remove the player from: ')
            for idx, team in enumerate(hockey_teams):
                if team['name'] == team_name:
                    hockey_teams[idx].roster.pop(player)
            else:
                print('team does not exist')

        elif choice == '4':
            name, position, number = input('Enter Team Name to list Team Roster: ')
            roster = {}
            roster['player_name'] = name
            roster['position'] = position
            roster['player_number'] = number
            print(roster)
            
            

        

if __name__ == "__main__":
    main()

my_team = HockeyTeam('Toronto Maple Leafs', 'East', 'Atlantic')
print(my_team)