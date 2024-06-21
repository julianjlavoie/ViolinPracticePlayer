# from pydub import AudioSegment
# from pydub import playback
import os


# TODO: add git integration, both local and web
# TODO: Use curses module to make terminal more interactive. https://docs.python.org/3/library/curses.html

# WelcomeScreen
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
# song = AudioSegment.from_mp3('soundFiles/Minuet2Bach.mp3')

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
