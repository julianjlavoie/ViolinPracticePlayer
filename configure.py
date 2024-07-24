"""
Author: Julian lavoie
"""

import os
import json
from pydub import AudioSegment
from pydub import playback


# HOME_PATH = os.path.expanduser("~")
# path_of_dir = os.fspath(f"{HOME_PATH}/Music/Pieces")
# song = AudioSegment.from_mp3(f"{path_of_dir}/22_Gavotte.mp3")
# #   This util will get artist and all meta data
# print(utils.mediainfo(f"{path_of_dir}/01_Twinkle_Twinkle_Little_Star_Variation_A.mp3"))


def configure(file, ftype):
    """
    Configure segments for a piece playback
    """
    # Set song to AudioSegment
    HOME_PATH = os.path.expanduser("~")
    path_of_dir = os.fspath(f"{HOME_PATH}/Music/{ftype.capitalize()}")

    song = AudioSegment.from_mp3(f"{path_of_dir}/{file}")
    song_length = song.duration_seconds * 1000
    # Setup segments list
    segments = [[0.0, 0.0]]
    print("What duration should I use to test segments? ")
    seconds = float(input())
    segments[0][1] = seconds
    print("What is the title of  this config?")
    config_title = input()

    # TODO: add option to replay a segment
    # TODO: add the segment beg and end to prompt for reference
    # TODO: add elapsed time to prompts and remaining time
    # TODO: how do i get time remaining and elapsed time? would that be better than song.duration_seconds
    # TODO: add segments[] to the json file

    segment_index = 0
    last_end = 0
    while segments[-1][1] < song_length / 1000:
        seg_done = False

        if segment_index != 0:
            segments.insert(
                segment_index,
                [
                    segments[segment_index - 1][1],
                    segments[segment_index - 1][1] + segments[0][1],
                ],
            )

        while seg_done is not True:
            playback.play(
                song[
                    segments[segment_index][0]
                    * 1000 : segments[segment_index][1]
                    * 1000
                ]
            )
            print(f"Piece Length: {song_length/1000}")
            print(f"Start:End (sug. {last_end}:{last_end+10}): ")
            response = input().split(":")
            segments[segment_index][0] = float(response[0])
            segments[segment_index][1] = float(response[1])
            last_end = float(response[1])
            # playback.play(song[segments[segment_index][0]*1000:segments[segment_index][1]*1000])
            print("Done? (y/n)")
            response = input()
            if response == "y".lower():
                seg_done = True

        segment_index += 1

    # TODO: create entry for piece in piece_config.json

    # Try read config
    try:
        # Read config
        with open("piece_config.json", "r+", encoding="utf-8"):
            pass
    except IOError as i:
        print(i)
        print("Creating new piece_config")
        with open("piece_config.json", "w") as write_file:
            # Add an array
            json.dump({}, write_file)
    finally:
        # save file content to config_file
        with open("piece_config.json", "r+", encoding="utf-8") as reading_file:
            config_file = json.load(reading_file)

    config_file[file.split(".")[0]] = {
        "file": file,
        "file_type": ftype,
        "configs": {config_title: []},
    }
    formated_segs = [f"{s[0]}:{s[1]}" for s in segments]

    for i, s in enumerate(formated_segs, start=0):
        config_file[file.split(".")[0]]["configs"][config_title].append(s)

    # Write new config entry to piece_config
    with open("piece_config.json", "w") as file:
        json.dump(config_file, file)
