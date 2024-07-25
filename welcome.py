"""
Author: Julian Lavoie
"""

import os
import json

HOME_PATH = os.path.expanduser("~")
PIECES_PATH = os.fspath(f"{HOME_PATH}/Music/Pieces")
ACCOMPANIMENTS_PATH = os.fspath(f"{HOME_PATH}/Music/Accompaniments")


def welcome():
    """
    WelcomeScreen
    """
    # -Menu
    # TODO: Secondary- sort list on recent plays, mastery score, some quantifiable data.

    pieces = sorted(os.listdir(PIECES_PATH))
    accompaniments = sorted(os.listdir(ACCOMPANIMENTS_PATH))
    has_config = False

    # DONE: List pieces by name of files in mp3 directory. Exclude extension.
    print("Pieces\n" + "---------------")
    for i, p in enumerate(pieces):
        piece = p.rstrip(".mp3")
        print(f"{i:3d}: {piece}")

    print("\nAccompaniment\n" + "---------------")
    for i, a in enumerate(accompaniments):
        accompaniment = a.rstrip(".mp3")
        print(f"{i:3d}: {accompaniment}")

    action = (
        "configure"
        if input("What do you want to do? Configure or Play c/P ").lower() == "c"
        else "play"
    )

    returned_piece = int(input("Choose a practice piece Def. 0: "))

    piece_type = (
        "accompaniments"
        if input("Pieces or Accompaniments P/a ").lower() == "a"
        else "pieces"
    )

    if piece_type == "accompaniments":
        piece_choice = accompaniments[returned_piece]
    else:
        piece_choice = pieces[returned_piece]

    # Is there a matching piece config in the database?
    # if no prompt to create one, continue without segmentation, choose another piece
    # Try read config
    try:
        # Read config
        with open("piece_config.json", "r+", encoding="utf-8") as read_file:
            pass
    except IOError as i:
        print(i)
        print("Creating new piece_config")
        with open("piece_config.json", "w") as write_file:
            # Add an array
            json.dump({}, write_file)
    finally:
        with open("piece_config.json", "r+", encoding="utf-8") as read_file:
            config_file = json.load(read_file)

    if config_file.get(piece_choice.split(".")[0] is None):
        response = input(
            "This piece has not been configured. Would you like to configure now? "
        ).lower()
        if response == "y":
            action = "configure"
    else:
        has_config = True

    return action, piece_choice, piece_type, has_config
