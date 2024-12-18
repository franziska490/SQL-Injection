import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3
from anvil.files import data_files

#Datenbankdatei verwenden
DATABASE = anvil.files.data_files['database.db']

#Funktion zur Verbindung mit SQLite
def connect_db():
  return sqlite3.connect(DATABASE)

#Login-Funktion für Level 1 (Unsicher)
@anvil.server.callable
def login(username, password):
  db = connect_db()
  cursor = db.cursor()
  query = f"SELECT username FROM Users WHERE username = '{Username}'AND password = '{password}'"
  try:
    user = cursor.execute(query).fetchone()
    db.close()
    if user:
      return user[0]
    return None
  except Exception as e:
    db.close()
    return f"Error: {e}"


#Kontostand abrufen
@anvil.server.callable
def get_balance(account_no):
  db = connect_db()
  cursor = db.cursor()
  query = f"SELECT balance FROM Balances WHERE AccountNO = {account_no}"
  try:
    balance = cursor.execute(query).fetchone()
    db.close()
    return balance[0] if balance else None
  except Exception as e:
    db.close()
    return f"Error: {e}"

@anvil.server.callable
def secure_login(username, password):
  db = connect_db()
  cursor = db.cursor()
  try:
    #Verwende Prepared Statements für Sicherheit
    query = "SELECT username FROM Users WHERE username = ? AND password = ?"
    user = cursor.execute(query, (username, password)).fetchone()
    db.close
    return user[0] if user else None
  except Exception as e:
    db.close
    return f"Error: {e}"