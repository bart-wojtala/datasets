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
        print("Processing file: " + f)
        sound = AudioSegment.from_file(join(main_directory, f), format="wav")

        start_trim = detect_leading_silence(sound)
        end_trim = detect_leading_silence(sound.reverse())

        duration = len(sound)    
        trimmed_sound = sound[start_trim:duration - end_trim]
        output_audio = trimmed_sound + silence
        output_audio.export(join(clean_directory, f), format="wav")
    
def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=10):
    trim_ms = 0 # ms
    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms + chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms


if __name__ == "__main__":
    clip_files("/datasets/trump/wavs") # Set wavs directory here
