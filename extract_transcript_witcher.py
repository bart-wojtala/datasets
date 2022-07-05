import os
import shutil
from natsort import natsorted
from pyunpack import Archive


def is_bezi(text):
    other_index = text.find('other')
    if other_index == -1:
        other_index = text.find('hero')
    self_index = text.find('self')
    if other_index < self_index:
        return True
    return False


if __name__ == '__main__':
    target_voice = 'GodlingJohnny'
    speaker_number = '15'
    transcript_file = 'witcher_transcript_cleared.txt'
    main_directory = 'datasets/flowtron/Wiedzmin 3/'
    source_directory = main_directory + target_voice + '/'
    dataset_directory = source_directory + target_voice
    wavs_directory = dataset_directory + '/wavs/'
    target_directory = 'datasets/flowtron/wavs_wiedzmin/'
    source_transcript_file = 'list.txt'
    transcript = {}

    Archive(source_directory + target_voice + '.7z').extractall(source_directory)

    with open(os.path.join(dataset_directory, source_transcript_file), 'r', encoding='utf-8') as f:
        content = f.readlines()
        for line in content:
            line_split = line.split('|')
            filename = line_split[0][5:].strip()
            text = line_split[1].strip()
            if text not in transcript.values():
                transcript[filename] = text

    files = [f for f in os.listdir(wavs_directory) if os.path.isfile(
        os.path.join(wavs_directory, f))]
    sorted_files = natsorted(files)

    with open(transcript_file, 'w', encoding='utf-8') as output_file:
        for f in sorted_files:
            if f in transcript.keys():
                line_to_write = 'wavs/' + f + '|' + transcript[f] + '|' + speaker_number + '\n'
                output_file.write(line_to_write)

    for filename in os.listdir(wavs_directory):
        if filename in transcript.keys():
            source = os.path.join(os.getcwd(), wavs_directory + filename)
            target = os.path.join(os.getcwd(), target_directory)
            shutil.copy(source, target)
