from ui.mainwindow import startui
from controller import Controller
import sys

try:
    if sys.argv[1] == "--help":
        print(f"""{sys.argv[0]} help
              \nThis program only supports this arguments
              \n--help Print this message
              \n--noTkinter dont use Tkinter
              """)
        exit
except IndexError:    
    startui(Controller())