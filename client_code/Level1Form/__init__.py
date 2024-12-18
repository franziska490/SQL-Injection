from ._anvil_designer import Level1FormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil import alert



class Level1Form(Level1FormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def login_button_click(self, **event_args):
    username = self.username_box.text
    password = self.password_box.text

    if not username or not password:
      anvil.alert("Bitte fülle beide Felder aus!", title="Fehler")
      return

    #Server-Funktion 'login' aufrugen
    user = anvil.server.call('login', username, password)

    if user:
      anvil.alert(f"Willkommen, {user}!", title="Erfolg")
      #Weiter zu Level 2
      open_form('Level2Form')
    else:
      self.error_label.text = "Login fehlgeschlagen! Falsche Eingabe"
      
