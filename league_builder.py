# Import CSV library.
import csv

# Define functions.
def read_csv(filename):
	with open(filename, newline='') as csvfile:
		player_reader = csv.DictReader(csvfile, delimiter=',')
		player_data = list(player_reader)
	return player_data

if __name__ == "__main__":
	# Program will read CSV file. The output will be lists of dictionaries.
	player_data = read_csv("soccer_players.csv")

	# Separate experienced and non-experienced players.
	yes_exp_players = []
	no_exp_players = []
	for row in player_data:
		if row ["Soccer Experience"] == "YES":
			yes_exp_players.append(row)
		else:
			no_exp_players.append(row)

	# Divide players by experience and assign them to teams.
	no_exp1 = no_exp_players[:3]
	no_exp2 = no_exp_players[3:6]
	no_exp3 = no_exp_players[6:9]
	exp1 = yes_exp_players[:3]
	exp2 = yes_exp_players[3:6]
	exp3 = yes_exp_players[6:9]
	sharks = no_exp1 + exp1
	dragons = no_exp2 + exp2
	raptors = no_exp3 + exp3

	# Create "teams.txt" and write team rosters to file.
	with open("teams.txt", "w") as file:
		file.write("Sharks\n")
		for player in sharks:
			file.write("{Name}, {Soccer Experience}, "
				"{Guardian Name(s)}\n".format(**player))
		file.write("\nDragons\n")
		for player in dragons:
			file.write("{Name}, {Soccer Experience}, "
				"{Guardian Name(s)}\n".format(**player))
		file.write("\nRaptors\n")
		for player in raptors:
			file.write("{Name}, {Soccer Experience}, "
				"{Guardian Name(s)}\n".format(**player))

	# Extra Credit
	# Add team name to dictionary 
	for player in sharks:
		player["Team Name"] = "Sharks"
	for player in dragons:
		player["Team Name"] = "Dragons"
	for player in raptors:
		player["Team Name"] = "Raptors"

	new_player_data = sharks + dragons + raptors

	# Create "Welcome letters" for each team for the guardians.
	for player in new_player_data:
		file_name = "_".join(player["Name"].lower().split()) + ".txt"
		with open(file_name, "w") as file:
			file.write("Dear {Guardian Name(s)},\n\n".format(**player))
			file.write("Your child, {Name}, has been selected to play on\n"
				"the {Team Name}! The {Team Name} first practice is on \n"
				"Saturday, December 1, 2018 at 10:00am. Can't wait to see\n"
				"{Name} there!\n".format(**player))
			file.write("\nSincerely,\n\nYour Soccer League")