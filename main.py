#!/usr/bin/python

from gi.repository import Gtk
import id3_process

class App():

  def __init__(self):
    
    #Load layout from XML
    self.builder = Gtk.Builder()
    self.builder.add_from_file("gui/main_layout.glade")
    self.window = self.builder.get_object('top_window')

    #Connect close event to Gtk.main_quit
    self.window.connect("delete-event", Gtk.main_quit)
    
    #Map glade handler names to functions
    self.handlers = {"id3_toggled": self.toggle_id3,
                     "rename_toggled": self.toggle_rename,
                     "begin_clicked": self.process_files}
    self.builder.connect_signals(self.handlers)
   
    #Show
    self.window.show_all()
  

  def process_files(self, widget):
    directory = self.builder.get_object('dir_chooser').get_filename()
    id3_process.process_files(directory)
    

  #Callback for toggle event on id3_check
  #Toggles sensitivity of id3-related widgets
  def toggle_id3(self, widget):
    #Toggle sensitivity for related widgets
    state = self.builder.get_object('id3_check').get_active()
    self.builder.get_object('framecode_entry').set_sensitive(state) 
    self.builder.get_object('tags_grid').set_sensitive(state)
    #Enable Start button when this and/or rename_check are active
    if (state):
      self.builder.get_object('process_button').set_sensitive(True)
    elif (self.builder.get_object('rename_check').get_active() == False):
      self.builder.get_object('process_button').set_sensitive(False)
  

  #Callback for toggle event on rename_check
  #Toggles sensitivity of rename-related widgets
  def toggle_rename(self, widget):
    #Toggle sensitivity for related widgets
    state = self.builder.get_object('rename_check').get_active()
    self.builder.get_object('pattern_box').set_sensitive(state) 
    #Enable Start button when this and/or id3_check are active
    if (state):
      self.builder.get_object('process_button').set_sensitive(True)
    elif (self.builder.get_object('id3_check').get_active() == False):
      self.builder.get_object('process_button').set_sensitive(False)


#If invoked directly
if __name__ == "__main__":
  app = App()
  Gtk.main()
