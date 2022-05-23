import pypinyin
import argparse

parser = argparse.ArgumentParser(description='Parse IO file names.')
parser.add_argument('--input', type=str, help='path to the file with labels')
parser.add_argument('--output', type=str, help='path to the output file')

args = parser.parse_args()

read_file_name = args.input
write_file_name = args.output

buffer = []
with open(read_file_name, 'r') as file:
    for line in file:
        line = line.strip()
        if not line or line[0] == '\n' or line[0] == '#':
            continue

        l = line[:-1].split(' ')
        filename, character = l

        pred = pypinyin.pinyin(character, style=pypinyin.Style.NORMAL, neutral_tone_with_five=True)
        pred = [p[0] for p in pred]
        pred = ''.join(pred)
        pred = pred.upper()
        # print(pred)

        buffer.append(' '.join([filename, pred]))
        

with open(write_file_name,'w') as ef:
    buffer = '\n'.join(buffer)
    ef.write(buffer)
