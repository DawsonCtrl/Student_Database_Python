from flask import Flask, render_template
import sqlite3

app = Flask(__name__, template_folder='C:/Users/dawso/Documents/GitHub/Student_Database_Python/StudentDB/templates')

# SQLite database file
db_name = '"studentsDB.db"'

# Function to get data from the database
def get_data_from_db(query):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows

# Route for the index page
@app.route('/')  # This links the function to the home route
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
