#!/usr/bin/python

from gi.repository import Gtk

class App():

  def __init__(self):
    self.builder = Gtk.Builder()
    self.builder.add_from_file("this3.glade")
    self.window = self.builder.get_object('window1')
    self.window.show_all()


app = App()
Gtk.main()
