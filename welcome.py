'''
Author: Julian Lavoie
'''
import os

HOME = os.path.expanduser("~")
PIECES = os.fspath(f"{HOME}/Music/Pieces")
ACCOMPANIMENTS = os.fspath(f"{HOME}/Music/Accompaniments")

def welcome() -> (str, str, str):
    """
        WelcomeScreen
    """
    # -Menu
    print("Choose a practice piece: \n")

    # TODO: sort list on recent plays, mastery score, some quantifiable data.

    pieces = os.listdir("soundFiles")[1:]

    # DONE: List pieces by name of files in mp3 directory. Exclude extension.
    for i, p in enumerate(pieces):
        piece = p.rstrip(".mp3")
        print(f"{i}: {piece}")

    piece_choice = input("\n")
    # TODO: Is there a matching piece config in the database?
    return "","",""
