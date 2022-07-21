import os


if __name__ == '__main__':
    wavs_directory = 'datasets/flowtron/wavs/'
    file_list = 'list.txt'
    file_list_cleared = 'witcher_transcript_cleared.txt'
    textlines = {}
    files_in_transcript = []
    duplicates = []
    uppercase = []

    with open(file_list, 'r', encoding='utf-8') as f:
        content = f.readlines()

    for i, line in enumerate(content):
        file = line.split('|')[0][5:]
        text = line.split('|')[1]
        if text in textlines.values():
            duplicates.append(text + '|' + line.split('|')[2])
        try:
            textlines[file] = text + '|' + line.split('|')[2]
        except IndexError:
            print(text)
        files_in_transcript.append(file)

        for word in text.split(' '):
            if word.isupper() and word not in ['A', 'E', 'I', 'O', 'U', 'W', 'Z']:
                uppercase.append(line)
                break

    # Delete files that don't exist in transcript (run after files are copies)
    for filename in os.listdir(wavs_directory):
        if filename not in files_in_transcript:
            os.remove(os.path.join(wavs_directory, filename))
        else:
            files_in_transcript.remove(filename)

    print(files_in_transcript)
    print(duplicates)
    print(uppercase)
