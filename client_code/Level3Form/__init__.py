from ._anvil_designer import Level3FormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import alert



class Level3Form(Level3FormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def login_button_click(self, **event_args):
    username = self.username_box.text
    password = self.password_box.text

    if not username or not password:
      self.error_label.text = "Bitte alle Felder ausfüllen!"
      return

    #Sichere Server-Funktion aufrufen
    user = anvil.server.call('secure_login', username, password)

    if user:
      anvil.alert(f"Herzlichen Glückwunsch, {user}! Du hast Level 3 bestanden!", title="Erfolg")
    else:
      self.error_label.text = "Login fehlgeschlagen! Ungültige Eingaben."
