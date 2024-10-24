import sqlite3
import pandas as pd

# Load the cleaned Excel file
df = pd.read_excel('data/cleaned_translations.xlsx')

# Connect to SQLite database
conn = sqlite3.connect('translations.db')
cursor = conn.cursor()

# Drop the table if it already exists
cursor.execute('DROP TABLE IF EXISTS translations')

# Create the table again
cursor.execute('''
    CREATE TABLE translations (
        word TEXT PRIMARY KEY,
        translation TEXT
    )
''')

# Insert cleaned data into the database
for index, row in df.iterrows():
    word = row['English']  # Adjust to 'English' column
    translation = row['Tulu']  # Adjust to 'Tulu' column
    cursor.execute('INSERT OR REPLACE INTO translations (word, translation) VALUES (?, ?)', (word, translation))

# Commit the changes and close the connection
conn.commit()
conn.close()

print('Data successfully loaded into the database.')
