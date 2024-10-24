import sqlite3
import pandas as pd

# Load the Excel file
df = pd.read_excel('data/translations.xlsx', header=1)
df.columns = ['SL. No.', 'English', 'Tulu']
df = df[['English', 'Tulu']]
df['English'] = df['English'].str.strip().str.lower()


print("Cleaned DataFrame:\n", df.head())
print("Column names:", df.columns.tolist())

# Connect to SQLite database
conn = sqlite3.connect('translations.db')
cursor = conn.cursor()

# Drop the table if it exists
cursor.execute('DROP TABLE IF EXISTS translations')

# Create the translations table
cursor.execute('''
    CREATE TABLE translations (
        word TEXT PRIMARY KEY,
        translation TEXT
    )
''')

# Insert cleaned data into the database
for index, row in df.iterrows():
    word = row['English']
    translation = row['Tulu']
    cursor.execute('INSERT OR REPLACE INTO translations (word, translation) VALUES (?, ?)', (word, translation))

# Commit the changes and close the connection
conn.commit()
conn.close()

print('Data successfully loaded into the database.')
