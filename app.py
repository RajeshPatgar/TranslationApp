from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def get_translation(word):
    # Connect to the SQLite database
    conn = sqlite3.connect('translations.db') 
    cursor = conn.cursor()
    
    # Fetch the translation
    cursor.execute("SELECT translation FROM translations WHERE word = ?", (word,))
    result = cursor.fetchone() 
    conn.close()
    
    return result[0] if result else None  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    word = request.form['word'].strip().lower()  
    translation = get_translation(word)  
    if translation is None:
        translation = "No translation found for '{}'.".format(word) 
    return render_template('index.html', translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
