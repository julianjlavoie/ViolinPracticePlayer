"""
Author: Julian lavoie
"""

import os
import json
from pydub import AudioSegment

# from pydub import playback
from play import play_seg


def configure(file, ftype):
    """
    Configure segments for a piece playback
    """
    # Set song to AudioSegment
    HOME_PATH = os.path.expanduser("~")
    path_of_dir = os.fspath(f"{HOME_PATH}/Music/{ftype.capitalize()}")
    song = AudioSegment.from_mp3(f"{path_of_dir}/{file}")

    # save file content to config_file
    with open("piece_config.json", "r+", encoding="utf-8") as reading_file:
        config_file = json.load(reading_file)

    song_length = song.duration_seconds * 1000
    # Setup segments list
    segments = [[0.0, 0.0]]
    seconds = float(input("What duration should I use to test segments? "))
    segments[0][1] = seconds
    print("Configs: ")

    try:
        configs = config_file[file.split(".")[0]]["configs"].keys()
        for i, n in enumerate(configs.keys()):
            print(f"{i}.{n} ")
    except Exception as e:
        print(f"No Configs Found! ({e})")

    config_title = input("What is the title of this config? ")

    # TODO:Primary- add option to replay a segment
    # Done: add the segment beg and end to prompt for reference
    # TODO:Secondary- add elapsed time to prompts and remaining time
    # how do i get time remaining and elapsed time? would that be better than song.duration_seconds

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
            play_seg(song, segments[segment_index][0], segments[segment_index][1])
            print(f"Piece Length: {song_length/1000}")
            seg_start_end = input(f"Start:End (sug. {last_end}:{last_end+10}): ").split(
                ":"
            )
            segments[segment_index][0] = float(seg_start_end[0])
            segments[segment_index][1] = float(seg_start_end[1])
            play_seg(song, segments[segment_index][0], segments[segment_index][1])
            seg_done = True
            last_end = float(seg_start_end[1])
        segment_index += 1

    # TODO: create entry for piece in piece_config.json

    config_file[file.split(".")[0]] = {
        "file": file,
        "file_type": ftype,
        "configs": {config_title: []},
    }
    formated_segs = [f"{s[0]}:{s[1]}" for s in segments]

    for s in formated_segs:
        config_file[file.split(".")[0]]["configs"][config_title].append(s)

    # Write new config entry to piece_config
    with open("piece_config.json", "w") as file:
        json.dump(config_file, file)
