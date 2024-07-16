'''
Author: Julian Lavoie
'''
from welcome import welcome
from play import play
from configure import configure


# TODO: add git integration, both local and web
# TODO: Use curses module to make terminal more interactive. 
# https://docs.python.org/3/library/curses.html
# TODO: Add an init for the pieces and accompaniment if not set
# TODO: ADD a print line with version, author, pieces directories

while True:
    action,file,ftype = welcome()
    if action == "play":
        play(file, ftype)
    if action == "configure":
        configure(file, ftype)
