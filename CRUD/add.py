import email
from os import name
from flask import Flask, render_template, request, redirect, url_for
from database import conn, cursor


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') # it simply run the index.html page, means it will show the index.html page


#------------------------add-----------------

@app.route('/add')
def add():
    return render_template('add.html')  # it simply run the add.html page, means it will show the add.html page

#------------------------insert-----------------

@app.route('/insert', methods =['POST'])
def insert():

    name = request.form['name']
    surname = request.form['surname']
    email = request.form['email']
    mobile = request.form['mobile']
    age = request.form['age']
    gender = request.form['gender']

    cursor = conn.cursor()

    query = "INSERT INTO users (name, surname, email, mobile, age, gender) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (name, surname, email, mobile, age, gender))
    conn.commit()
    cursor.close()

    return redirect(url_for('index'))



#------------------------view-----------------
@app.route('/view')
def view():

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return render_template('view.html', users=users)  # it simply run the view.html page, means it will show the view.html page


#-------------------------edit------------------------

@app.route('/edit/<int:id>')
def edit(id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    cursor.close()
    

    return render_template('edit.html', user=user)

#-------------------------update------------------------

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['name']
    surname = request.form['surname']
    email = request.form['email']
    mobile = request.form['mobile']
    age = request.form['age']
    gender = request.form['gender']

    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name=%s, surname=%s, email=%s, mobile=%s, age=%s, gender=%s WHERE id=%s", (name, surname, email, mobile, age, gender, id))
    conn.commit()
    cursor.close()
    
    return redirect(url_for("view"))

#-------------------------delete------------------------

@app.route('/delete/<int:id>')
def delete(id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    
    return redirect(url_for("view"))

if __name__ == '__main__':
    app.run(debug=True)

