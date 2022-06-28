import os
import re


def is_bezi(text):
    other_index = text.find('other')
    self_index = text.find('self')
    if other_index < self_index:
        return True
    return False


if __name__ == '__main__':

    main_directory = 'datasets/flowtron/Gothic 1-2 Skrypty/'
    dataset_subdirectories = ['MISSIONS/', 'Dialoge/']
    transcript_dict = {}

    for directory in dataset_subdirectories:
        dataset_directory = main_directory + directory
        for filename in os.listdir(dataset_directory):
            with open(os.path.join(dataset_directory, filename), 'r') as f:
                content = f.readlines()
                for line in content:
                    if 'AI_Output' in line:
                        line_split = line.split('//')
                        text = line_split[1].strip()
                        info = line_split[0].strip()
                        if is_bezi(info):
                            pattern = '([\"])([\w]+)([\"])'
                            filename = 'wavs/' + \
                                re.search(pattern, info).group(2) + '.wav'
                            transcript_dict[filename] = text

    with open('gothic_list.txt', 'w', encoding='utf-8') as output_file:
        for key, value in transcript_dict.items():
            line_to_write = key + '|' + value + '|' + '0' + '\n'
            output_file.write(line_to_write)
