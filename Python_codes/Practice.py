import pandas as pd

# Sample data with missing values, duplicates, and inconsistent formats
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Bob', 'Eve'],
    'Age': [25, None, 35, 45, 28, None, 28],
    'Salary': [50000, 60000, None, 80000, 55000, 60000, 55000],
    'Join Date': ['2020-01-01', '2019-06-15', None, '2021-03-10', '2019-06-15', '2019-06-15', '2019-06-15']
}

# Create a DataFrame
df = pd.DataFrame(data)

# 1. Display original DataFrame
print("Original DataFrame:\n",df)


# 2. Handling Missing Values
# Option 1: Fill missing values with mean or a default value
df['Age'].fillna(df['Age'].mean(), inplace=True)  # Filling missing age with the average age
df['Salary'].fillna(df['Salary'].mean(), inplace=True)  # Filling missing salary with average salary
df['Join Date'].fillna('Unknown', inplace=True)  # Filling missing join date with 'Unknown'

# Option 2: Drop rows with missing values (if filling is not appropriate)
# df.dropna(inplace=True)

print("\nDataFrame after handling missing values:")
print(df)

# 3. Removing Duplicates
# Remove duplicate rows based on all columns
df.drop_duplicates(inplace=True)

print("\nDataFrame after removing duplicates:")
print(df)

# 4. Data Transformation: Converting 'Join Date' to datetime format
# This ensures all dates are in a consistent format for analysis
df['Join Date'] = pd.to_datetime(df['Join Date'], errors='coerce')  # Convert valid dates, set invalid ones as NaT

print("\nDataFrame after transforming 'Join Date':")
print(df)

# 5. Additional Transformation: Creating a new column 'Experience' (Years since Join Date)
# Fill missing or invalid join dates with a default date (e.g., today's date)
df['Experience'] = pd.to_datetime('today').year - df['Join Date'].dt.year

print("\nDataFrame after adding 'Experience' column:")
print(df)

# 6. Renaming columns for consistency (optional)
df.rename(columns={'Join Date': 'Join_Date'}, inplace=True)

print("\nDataFrame with renamed columns:")
print(df)

# Final Cleaned DataFrame
print("\nFinal Cleaned DataFrame:")
print(df)
