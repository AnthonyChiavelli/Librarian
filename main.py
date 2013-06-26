#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class App:
  def __init__(self):
    #Create a new window for application
    self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    #Connect events to event handler functions
    self.window.connect("delete_event", self.delete_event)
    self.window.connect("destroy", self.destroy)

    #Test button
    self.button = gtk.Button("Test")
    self.button.connect("clicked", self.clicked, None)
    self.window.add(self.button)
    self.button.show()

    self.window.show()

  def clicked(self, widget, data=None):
    print "Clicked"

  #Callback function connected to titlebar close 
  def delete_event(self):
    return False #True to remain open

  #Callback function connected to gtk_widget_destroy() call
  #or False returned from self.delete_event()
  def destroy(self, widget, data=None):
    gtk.main_quit()

  def main(self):
    gtk.main()


#If invoked directly
if __name__ == "__main__":
  app = App()
  app.main()
  print "Librarian"

