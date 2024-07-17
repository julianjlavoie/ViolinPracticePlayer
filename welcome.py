'''
Author: Julian Lavoie
'''
import os

HOME_PATH = os.path.expanduser("~")
PIECES_PATH = os.fspath(f"{HOME_PATH}/Music/Pieces")
ACCOMPANIMENTS_PATH = os.fspath(f"{HOME_PATH}/Music/Accompaniments")

def welcome() -> (str, str, str):
    """
        WelcomeScreen
    """
    # -Menu
    # TODO: sort list on recent plays, mastery score, some quantifiable data.

    pieces = sorted(os.listdir(PIECES_PATH))
    accompaniments = sorted(os.listdir(ACCOMPANIMENTS_PATH))

    # DONE: List pieces by name of files in mp3 directory. Exclude extension.
    print("Pieces\n"+"---------------")
    for i, p in enumerate(pieces):
        piece = p.rstrip(".mp3")
        print(f"{i:3d}: {piece}")

    print("\nAccompaniment\n"+"---------------")
    for i, a in enumerate(accompaniments):
        accompaniment = a.rstrip(".mp3")
        print(f"{i:3d}: {accompaniment}")

    # -Prompt
    actions = ["configure", "play"]

    print(f"What do you want to do? ({actions})")
    action = input().lower()

    print("\nChoose a practice piece: \n")
    returned_piece = int(input())

    print("Pieces or Accompaniments")
    piece_type = input().lower()

    if piece_type == "pieces":
        piece_choice = pieces[returned_piece]

    # TODO: Primary(1) -Is there a matching piece config in the database? 
    # if yes return it 
    # if no prompt to create one, continue without segmentation, choose another piece
    

    return action,piece_choice,piece_type
