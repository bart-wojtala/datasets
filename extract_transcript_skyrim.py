import os
import shutil
from natsort import natsorted
from pyunpack import Archive
from pydub import AudioSegment


if __name__ == '__main__':
    target_voice = 'maledarkelf'
    speaker_number = '47'
    transcript_file = 'skyrim_transcript_cleared.txt'
    main_directory = 'datasets/flowtron/Skyrim/Vanilla/'
    source_directory = main_directory + target_voice + '/'
    dataset_directory = source_directory + target_voice
    wavs_directory = dataset_directory + '/' + target_voice + '/'
    target_directory = 'datasets/flowtron/wavs_skyrim/'
    source_transcript_file = target_voice + '.txt'
    transcript = {}
    long_files = []

    Archive(source_directory + target_voice +
            '.7z').extractall(source_directory)

    with open(os.path.join(dataset_directory, source_transcript_file), 'r', encoding='utf-8') as f:
        content = f.readlines()
        for line in content:
            line_split = line.split('|')
            filename = line_split[0].strip().lower()
            text = line_split[1].strip()
            if text not in transcript.values():
                transcript[filename] = text

    files = [f for f in os.listdir(wavs_directory) if os.path.isfile(
        os.path.join(wavs_directory, f))]
    sorted_files = natsorted(files)

    with open(transcript_file, 'w', encoding='utf-8') as output_file:
        for f in sorted_files:
            if f in transcript.keys():
                line_to_write = 'wavs/' + f + '|' + \
                    transcript[f] + '|' + speaker_number + '\n'
                output_file.write(line_to_write)

    for filename in os.listdir(wavs_directory):
        if filename in transcript.keys():
            source = os.path.join(os.getcwd(), wavs_directory + filename)
            target = os.path.join(os.getcwd(), target_directory)
            shutil.copy(source, target)

    for filename in os.listdir(target_directory):
        if filename.endswith('.wav'):
            w = AudioSegment.from_wav(os.path.join(target_directory, filename))
            if len(w) > 10000:
                long_files.append(filename)

    for f in long_files:
        print(f)
