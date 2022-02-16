from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Message:
  def __init__(self,data):
    self.id = data['id']
    self.content = data['content']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.user_id = data['user_id']
    self.recipient_id = data['recipient_id']
    self.sender_name = user.User.get_name_by_id(data['user_id'])
    
    self.creator = None # this is the associated data list

  # CREATE

  @classmethod
  def save(cls,data):
    query = "INSERT INTO messages (content, user_id, recipient_id) VALUES(%(content)s, %(user_id)s, %(recipient_id)s);"
    return connectToMySQL('wall_schema').query_db(query,data)

  @classmethod
  def create_message(cls,data): # creating the message
    query = """
    INSERT INTO messsages (content, sender_id, recipient_id)
    VALUES (%(content)s, %(sender_id)s, %(recipient_id)s)
    ;"""
    return connectToMySQL('wall_schema').query_db(query,data)

  # READ

  @classmethod
  def get_all(cls):
    query = """SELECT * FROM messages;"""
    result = connectToMySQL('wall_schema').query_db(query)
    emails = []
    for row in result:
      emails.append(cls(row))
    return result

  @classmethod
  def get_by_id(cls, data):
    messages = []
    query = "SELECT * FROM messages WHERE recipient_id = %(id)s;"
    results = connectToMySQL('wall_schema').query_db(query, data)
    for note in results:
      messages.append(cls(note))
    return messages

  # UPDATE

  @classmethod
  def update(cls, data):
    query = "UPDATE * FROM users WHERE id = %(id)s"
    data = {
      "id" : id,
    }
    results = connectToMySQL('wall_schema').query_db(query, data)
    return cls(results[0])

  # DELETE

  @classmethod
  def delete(cls, id):
    query = "DELETE FROM messages WHERE id = %(id)s"
    data = { 
      "id" : id
    }
    return connectToMySQL('wall_schema').query_db(query,data)