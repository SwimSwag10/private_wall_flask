from flask import render_template,request, redirect, flash, session
from flask_app import app
from flask_app.models.message import Message
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# CREATE

@app.route('/create/message', methods=['POST'])
def create_message():
  data ={ 
    "content": request.form['content'],
    "user_id": request.form['user_id'],
    "recipient_id": request.form['recipient_id'],
  }
  Message.save(data) # inserting the message into the database
  return redirect('/dashboard')

# READ

# UPDATE

# DELETE

@app.route('/delete/message/<int:id>')
def delete_message(id):
  Message.delete(id)
  return redirect('/dashboard')