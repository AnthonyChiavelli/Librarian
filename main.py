#!/usr/bin/python

from gi.repository import Gtk

class App():

  def __init__(self):
    
    #Load layout from XML
    self.builder = Gtk.Builder()
    self.builder.add_from_file("gui/main_layout.glade")
    self.window = self.builder.get_object('top_window')

    #Connect close event to Gtk.main_quit
    self.window.connect("delete-event", Gtk.main_quit)
    
    #Map glade handler names to functions
    self.handlers = {"id3_toggled": self.toggle_id3}
    self.builder.connect_signals(self.handlers)
    
    #Show
    self.window.show_all()
    

  #Callback for toggle event on id3_checkbox
  #Toggles sensitivity of id3-related widgets
  def toggle_id3(self, widget):
    #Toggle sensitivity 
    state = not widget.get_sensitive()
    self.builder.get_object('framecode_entry').set_sensitive(state)
    


#If invoked directly
if __name__ == "__main__":
  app = App()
  Gtk.main()
