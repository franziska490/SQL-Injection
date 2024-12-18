from ._anvil_designer import Level2FormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import alert



class Level2Form(Level2FormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def login_button_click(self, **event_args):
    username = self.username_box.text
    password = self. password_box.text

    #Verhindere einfache SQL-Injection durch Filterung
    if "'" in username or "'" in password:
      self.error_label.text = "Ungülige Eingabe! Zeichen ' sind nicht erlaubt."
      return

    user = anvil.server.call('login', username, password)

    if user:
      anvil.alert(f"Willkommen, {user}! Level 2 bestanden!", title="Erfolg")
      open_form('Level3From')
    else:
      self.error_label.text = "Login fehlgeschlagen! Ungültige Eingaben."