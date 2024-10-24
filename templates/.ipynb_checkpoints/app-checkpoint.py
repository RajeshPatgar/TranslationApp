from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Function to fetch translation from the database
def get_translation(word):
    conn = sqlite3.connect('translations.db')
    cursor = conn.cursor()
    cursor.execute('SELECT translation FROM translations WHERE TRIM(LOWER(word)) = TRIM(LOWER(?))', (word,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Route to handle form submission and show translation
@app.route('/', methods=['GET', 'POST'])
def index():
    translation = None
    if request.method == 'POST':
        english_word = request.form.get('english_word')  # Get the word from the form input
        translation = get_translation(english_word)  # Fetch the Tulu translation
        if not translation:
            translation = f"No translation found for '{english_word}'!"
    return render_template('index.html', translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
