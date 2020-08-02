import os
from os import listdir, makedirs
from os.path import isfile, join, exists
from pydub import AudioSegment

def clip_files(directory):
    main_directory = os.getcwd() + directory

    clean_directory = os.getcwd() + directory + "_clean"

    if not exists(clean_directory):
        makedirs(clean_directory)

    silence = AudioSegment.silent(duration = 100)
    files = [f for f in listdir(main_directory) if isfile(join(main_directory, f))]
    for f in files:
        input_audio = AudioSegment.from_wav(join(main_directory, f))
        output_audio = input_audio + silence
        output_audio.export(join(clean_directory, f), format="wav")
    

if __name__ == "__main__":
    clip_files("/datasets/trump/wavs")