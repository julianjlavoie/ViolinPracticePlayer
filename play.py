"""
Author: Julian Lavoie
"""
from pydub import AudioSegment
from pydub import playback
import os

def play(file, ftype):
    """
    Play a file
    """
    HOME_PATH = os.path.expanduser("~")
    path_of_dir = os.fspath(f"{HOME_PATH}/Music/{ftype.capitalize()}")

    song = AudioSegment.from_mp3(f"{path_of_dir}/{file}")
    playback.play(song)
    # TODO Play in segments using config file

    # seconds = 5
    # seg_length = seconds * 1000
    # first_seg = song[0:seg_length]
    # last_seg_start = 0

    # num_segments = len(song)//10000
    # for i in range(1, num_segments+1):
    #     print(f"\n Segment {i}: ")
    #     playback.play(song[last_seg_start: seg_length*i])
    #     print("\n Practice the piece. Ill wait!")

    #     replay = input("\n Replay? (y/n): ")
    #     while replay == "y":
    #         playback.play(song[last_seg_start: seg_length*i])
    #         replay = input("\n Replay? (y/n): ")

    #     last_seg_start = seg_length*i
