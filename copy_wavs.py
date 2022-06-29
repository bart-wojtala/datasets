import os
import shutil


if __name__ == '__main__':
    main_directory = 'datasets/flowtron/Gothic 1+2/'
    wavs_subdirectories = ['Gothic 1/wavs/', 'Gothic 2/wavs/']
    target_directory = 'datasets/flowtron/wavs/'
    file_list = 'gothic_list.txt'

    with open(file_list, 'r', encoding='utf-8') as f:
        content = f.readlines()

    for i, line in enumerate(content):
        content[i] = line.split('|')[0][5:].upper()

    for directory in wavs_subdirectories:
        dataset_directory = main_directory + directory
        for filename in os.listdir(dataset_directory):
            if filename in content:
                source = os.path.join(
                    os.getcwd(), dataset_directory + filename)
                target = os.path.join(os.getcwd(), target_directory)
                shutil.copy(source, target)
