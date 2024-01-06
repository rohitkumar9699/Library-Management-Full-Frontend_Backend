from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="project"
)

cursor = db.cursor()

# Route for the home page
@app.route('/')
def home():
    # Fetch data from the database
    cursor.execute("SELECT * FROM Book_det")
    books = cursor.fetchall()

    cursor.execute("SELECT * FROM Students_det")
    students = cursor.fetchall()

    cursor.execute("SELECT * FROM book_details")
    book_details = cursor.fetchall()

    cursor.execute("SELECT * FROM about_std")
    about_students = cursor.fetchall()

    # Render the HTML page with the data
    return render_template('index.html', books=books, students=students, book_details=book_details, about_students=about_students)

# Route for adding a new student
@app.route('/add_student', methods=['POST'])
def add_student():
    if request.method == 'POST':
        roll_no = request.form['roll_no']
        s_name = request.form['s_name']
        s_mob = request.form['s_mob']
        date_of_borrow = request.form['date_of_borrow']
        date_of_return = request.form['date_of_return']
        s_id = request.form['s_id']

        # Insert the data into the Students_det table using parameterized query
        cursor.execute("INSERT INTO Students_det (s_roll, s_name, s_mob, date_of_borrow, date_of_return, s_id) VALUES (%s, %s, %s, %s, %s, %s)",
                       (roll_no, s_name, s_mob, date_of_borrow, date_of_return, s_id))
        db.commit()

        return redirect(url_for('home'))

# Route for managing books
@app.route('/books')
def books():
    # Fetch data from the database using a JOIN query
    cursor.execute("SELECT * FROM Book_det bd JOIN book_details bdet ON bd.B_id = bdet.b_id")
    books = cursor.fetchall()

    # Render the HTML page with the data
    return render_template('books.html', books=books)


# Route for adding a new book
# ... (previous code) ...

# Route for adding a new book
@app.route('/add_book', methods=['POST'])
def add_book():
    if request.method == 'POST':
        b_id = request.form['b_id']  # Retrieve B_id from the form
        b_name = request.form['b_name']
        b_price = request.form['b_price']
        available = request.form['available']
        author = request.form['author']
        publisher = request.form['publisher']

        # Insert the data into the Book_det table using parameterized query
        cursor.execute("INSERT INTO Book_det (B_id, B_name, B_price, available) VALUES (%s, %s, %s, %s)",
                       (b_id, b_name, b_price, available))
        db.commit()

        # Insert the data into the book_details table using parameterized query
        cursor.execute("INSERT INTO book_details (b_id, author, publisher) VALUES (%s, %s, %s)",
                       (b_id, author, publisher))
        db.commit()

        return redirect(url_for('books'))

# ... (remaining code) ...


if __name__ == '__main__':
    app.run(debug=True)
