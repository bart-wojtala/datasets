import os


if __name__ == '__main__':
    punctuation = list(',.!?')
    letters = list('AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż ')
    symbols = punctuation + letters

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
        line_split = line.split('|')
        file = line_split[0][5:]
        text = line_split[1]
        id = line_split[2].strip()

        if '  ' in text:
            print('Double space in line: {}'.format(line))
            break
        if text[-1] not in symbols:
            print('Wrong text end symbol in line: {}'.format(line))
            break
        for char in text:
            if char not in symbols:
                print('Wrong character: {}, in line: {}'.format(char, line))
                break
        if not id.isdigit():
            print('Wrong character in speaker id in line: {}'.format(line))
            break

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
