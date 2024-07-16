'''
Author: Julian lavoie
'''

def configure(file, ftype):

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