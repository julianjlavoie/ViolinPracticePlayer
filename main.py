"""
Author: Julian Lavoie
"""

from welcome import welcome
from play import play
from configure import configure


# DONE: add git integration, both local and web
# TODO: Secondary -Use curses module to make terminal more interactive.
# https://docs.python.org/3/library/curses.html
# TODO: Secondary -prompt for the pieces and accompaniment directory paths if not set
# TODO: Secondary -ADD a print line with version, author, pieces directories

print("\n")

while True:
    action, file, ptype, has_config = welcome()
    if action == "play":
        play(file, ptype, has_config)
    if action == "configure":
        configure(file, ptype)
    print("______________________________________________________\n")
