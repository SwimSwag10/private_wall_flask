from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Message:
  def __init__(self,data):
    self.id = data['id']
    self.content = data['content']

  # CREATE

  @classmethod
  def save(cls,data):
    query = "INSERT INTO messages (content) VALUES(%(content)s)"
    return connectToMySQL('wall_schema').query_db(query,data)

  # READ

  @classmethod
  def get_all(cls):
    query = "SELECT * FROM messages"
    result = connectToMySQL('wall_schema').query_db(query)
    emails = []
    for row in result:
      emails.append(cls(row))
    return result

  @classmethod
  def get_by_id(cls,data):
    query = "SELECT * FROM messages WHERE id = %(id)s;"
    results = connectToMySQL('wall_schema').query_db(query,data)
    return cls(results[0])
  
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
  def delete(cls):
    query = "DELETE * FROM users WHERE id = %(id)s"
    results = connectToMySQL('wall_schema').query_db(query)
    return cls(results[0])