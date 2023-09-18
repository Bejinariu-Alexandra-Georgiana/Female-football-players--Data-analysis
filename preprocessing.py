import pandas as pd

# Load the dataset from a CSV file
df = pd.read_csv('goalscorers_new.csv')

# 1. Handling missing values
# Drop rows with missing values in any of the specified columns
columns_to_check_for_missing = ['date', 'home_team', 'away_team', 'team', 'scorer', 'minute', 'own_goal', 'penalty']
#print(columns_to_check_for_missing)
df.dropna(subset=columns_to_check_for_missing, inplace=True)

# 2. Handling duplicates
# Remove duplicate rows from the dataset
df.drop_duplicates(inplace=True)

# 3. Data consistency issues


# 4. Extract relevant columns
relevant_columns = ['date', 'home_team', 'away_team', 'team', 'scorer', 'minute', 'own_goal', 'penalty']
df = df[relevant_columns]

# 5. Data type conversions and standardizing data formats
# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Convert 'minute' column to integer
df['minute'] = df['minute'].astype(int)

# Ensure 'own_goal' and 'penalty' columns contain boolean values
df['own_goal'] = df['own_goal'].astype(bool)
df['penalty'] = df['penalty'].astype(bool)


print(df)