import pandas as pd

# Dataset
df = pd.read_csv('goalscorers_new.csv')

# Step 1: Calculate player statistics
player_stats = df.groupby('scorer').agg({
    'team': 'first',  # To get the team of the scorer
    'minute': 'sum',  # Total minutes played by the scorer
    'own_goal': 'sum',  # Total own goals scored by the scorer
    'penalty': 'sum',  # Total penalties scored by the scorer
}).reset_index()

# Step 2: Aggregate player statistics to create player profiles


# Step 3: Calculate metrics for player effectiveness
player_stats['goals_scored'] = df.groupby('scorer')['scorer'].transform('count')  # Total goals scored by the scorer
player_stats['goals_per_minute'] = player_stats['goals_scored'] / player_stats['minute']  # Goals per minute
player_stats['penalties_per_goal'] = player_stats['penalty'] / player_stats['goals_scored']  # Penalties per goal

# Display the player profiles with calculated metrics
print(player_stats[['scorer', 'team', 'goals_scored', 'minute', 'own_goal', 'penalty', 'goals_per_minute', 'penalties_per_goal']])