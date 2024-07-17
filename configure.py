'''
Author: Julian lavoie
'''
import os
from pydub import AudioSegment
from pydub import playback

def configure(file, ftype):
    """
    Configure segments for a piece playback
    """
    segments = [[0,0]]
    # TODO prompt segment length
    print("What duration should I use to test segments? ")
    seconds = int(input())
    segments[0][1] = seconds * 1000
    # TODO create entry for piece in piece_config.json
        # piece structure_____________
        # {title: <title>,
        # segments:
        # {0:{<beginning>,<ending>}},
        # {1:{<beginning>,<ending>}},
        # ...
        # }

    HOME_PATH = os.path.expanduser("~")
    path_of_dir = os.fspath(f"{HOME_PATH}/Music/{ftype.capitalize()}")

    song = AudioSegment.from_mp3(f"{path_of_dir}/{file}")
    beg = segments[0][0]
    end = segments[0][1]
    segment = song[beg:end]
    
    playback.play(segment)
    '''
    -if not, make one and begin the piece analysis
        -analysis: (new file with analysis code)
            -chunk the audio into 10sec?? bits and iterate through
            -each iteration will prompt if you want to repeat
            -finally prompt for the end time
            -the start time will be the iterations start time
            -the following iteration will start at the chosen end time from the 
            last iteration
            -the start and end time are written to the config json file in 
            track_configs
    if there is a config but it does not have all needed info start the analysis 
    with the found config file
    if there is a valid config file use it to  run through the practice sequence 
    below
    (move the practice sequence to its own file)
    after the piece you should be taken back tao the home menu
    ########## Actually   I want the config for each song to be in one json file 
    # named track_configs'''