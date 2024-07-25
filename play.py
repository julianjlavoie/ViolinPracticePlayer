"""
Author: Julian Lavoie
"""

from pydub import AudioSegment
from pydub import playback
import os
import json


def play_seg(song, seg_start, seg_end):
    not_done = True
    while not_done:
        playback.play(song[seg_start * 1000 : seg_end * 1000])
        not_done = True if input("Replay N/y: ").lower() == "y" else False


def play(file, ftype, has_config):
    """
    Play a file
    """
    HOME_PATH = os.path.expanduser("~")
    path_of_dir = os.fspath(f"{HOME_PATH}/Music/{ftype.capitalize()}")
    song = AudioSegment.from_mp3(f"{path_of_dir}/{file}")

    # Play with config or whole
    response = input("Play (w)hole piece or (c)onfigured segments? ")
    if has_config and response == "c":
        # get config file
        with open("piece_config.json", "r") as read_file:
            config = json.load(read_file)

        configs = config[file.split(".")[0]]["configs"]
        print("Configs: ")
        for i, n in enumerate(configs.keys()):
            print(f"{i}.{n} ")
        response = input("\nWhich config do you want to use? ")
        segs = config[file.split(".")[0]]["configs"][response]
        segments = []
        for p in segs:
            segments.append([float(p.split(":")[0]), float(p.split(":")[1])])
        for s in segments:
            play_seg(song, s[0], s[1])
            # not_done = True
            # while not_done:
            #     playback.play(song[s[0] * 1000 : s[1] * 1000])
            #     resp = input("Replay? Y/n: ").lower()
            #     if resp == "n":
            #         not_done = False
    else:
        playback.play(song)
