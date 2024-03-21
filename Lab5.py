# Cole McLean CSCI 161 MWF Class

player_names = []

goals = []

while True:
    player_name = input("Enter players name (or quit to exit) ")
    if player_name == 'quit':
        break
    player_names.append(player_name)
    goals.append(0)

num_players = len(player_names)
for i in range(num_players):
    true_goals = int(input(f"Enter the goals scored by {player_names[i]}: "))
    goals[i] = true_goals

print("Player stats:")
for i in range(num_players):
    print(f"{player_names[i]} - Goals: {goals[i]}")
