import os
import json
from collections import defaultdict


def json_extract(obj, key):
    '''Recursively fetch values from nested JSON.'''
    arr = []

    def extract(obj, arr, key):
        '''Recursively search for values of key in JSON tree.'''
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values


if __name__ == '__main__':
    dataset_directory = 'datasets/johnny_silverhand/'
    json_directory = dataset_directory + 'json_output/'
    original_transcript = defaultdict(str)

    with open(dataset_directory + 'metadata.csv', 'r') as f:
        transcript = f.readlines()

    for filename in os.listdir(json_directory):
        os.path.join(json_directory, filename)

        if 'onscreens' in filename:
            pass
        elif 'subtitles' in filename:
            pass
        else:
            with open(os.path.join(json_directory, filename), 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

            transcript_data = data['Chunks']

            for chunk in transcript_data:
                data = chunk['data']
                for key in data:
                    if key == 'Root':
                        root_data = data['Root']
                        entries = root_data['Reference']['data']['Entries']
                        if entries:
                            for entry in entries:
                                entry_id = entry['StringId']['Id']['val']
                                entry_text = ''
                                if entry['FemaleVariant'] != None:
                                    entry_text = entry['FemaleVariant']['val']
                                else:
                                    entry_text = entry['MaleVariant']['val']
                                original_transcript[entry_id] = entry_text

    with open('output.csv', 'w', encoding='utf-8') as output_file:
        for line in transcript:
            line_split = line.split('|')
            file_id = line_split[0][-20:-4]
            file_id_dec = int(file_id, 16)
            transcript_text = original_transcript[file_id_dec]
            line_to_write = line_split[0] + '|' + transcript_text + '\n'
            output_file.write(line_to_write)
