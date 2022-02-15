from flask import render_template,request, redirect, flash, session
from flask_app import app
from flask_app.models.message import Message
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# CREATE

@app.route('/create/message', methods=['POST'])
def create_message():
  data ={ 
    "content": request.form['content'],
  }
  Message.save(data) # inserting the message into the database
  # id = Message.save(data)
  # session['user_id'] = id
  return redirect('/dashboard')

# READ

# UPDATE

# DELETE

@app.route('/delete/message/<int:id>', methods=['POST'])
def create_message(id):
  data ={ 
    "id" : id,
  }
  Message.save(data) # inserting the message into the database
  # id = Message.save(data)
  # session['user_id'] = id
  return redirect('/dashboard')