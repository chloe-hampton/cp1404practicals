"""
Wimbledon
Estimate: 60 minutes
Actual: 2h 28 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        wimbledon_data = process_file(in_file)
        player_to_wins = count_player_wins(wimbledon_data)
    print_wimbledon_wins(player_to_wins, wimbledon_data)


def print_wimbledon_wins(player_to_wins, wimbledon_data):
    print("Wimbledon Champions:")
    for player, win_count in player_to_wins.items():
        print(f"{player} {win_count}")
    countries = sorted(set([country[1] for country in wimbledon_data]))
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(" ".join(countries))


def count_player_wins(wimbledon_data):
    player_to_wins = {}
    champions = {row[2] for row in wimbledon_data}
    for player in champions:
        win_count = 0
        for row in wimbledon_data:
            if row[2] == player:
                win_count += 1
        player_to_wins[player] = win_count
    return player_to_wins


def process_file(in_file):
    wimbledon_data = []
    in_file.readline()  # Skip header
    for line in in_file:
        # Make each row nested list
        row = line.strip().split(",")
        wimbledon_data.append(row)
    return wimbledon_data


main()
