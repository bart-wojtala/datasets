import os
import random
from pydub import AudioSegment


def split_data(transcript_file):
    main_directory = os.getcwd() + "\\datasets\\flowtron\\"
    wavs_directory = main_directory + "wavs\\"
    speakers = {}
    transcript_lines = []
    val_lines = []

    with open('flowtron_speakers.csv', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line_split = line.split('|')
            id = line_split[0]
            name = line_split[1].strip()
            speakers[id] = {'name': name, 'length': 0, 'line': ''}

    with open(os.path.join(os.getcwd() + transcript_file), 'r', encoding='utf-8') as f:
        transcript_lines = f.readlines()
        for line in transcript_lines:
            line_split = line.split('|')
            file = line_split[0][5:]
            id = line_split[2].strip()

            audio = AudioSegment.from_file(wavs_directory + file)
            length = audio.duration_seconds
            if length > speakers[id]['length']:
                speakers[id]['length'] = length
                speakers[id]['line'] = line

    for _, val in speakers.items():
        line = val['line']
        val_lines.append(line)
        transcript_lines.remove(line)
        print(val)

    random.shuffle(transcript_lines)

    with open(main_directory + 'dataset_val.txt', 'w', encoding='utf-8') as f:
        for line in val_lines:
            f.write(f'{line}')

    with open(main_directory + 'dataset_train.txt', 'w', encoding='utf-8') as f:
        for line in transcript_lines:
            f.write(f'{line}')


if __name__ == "__main__":
    split_data("/datasets/flowtron/list.txt")
