import pypinyin
import argparse

parser = argparse.ArgumentParser(description='Parse IO file names.')
parser.add_argument('--input', type=str, help='path to the file with labels')
parser.add_argument('--output', type=str, help='path to the output file')

args = parser.parse_args()

read_file_name = args.input
write_file_name = args.output
# read_file_name = '/Users/jasmineli/Desktop/wenet/examples/aishell/s0/vocab.txt'
# write_file_name = '/Users/jasmineli/Desktop/wenet/examples/aishell/s0/dict.txt'

buffer = []
seen = set()
with open(read_file_name, 'r') as file:
    for line in file:
        line = line.strip()
        if not line or line[0] == '\n' or line[0] == '#':
            continue

        l = line[:-1].split(' ')
        char, idx = l
        if char == '<sos/eos>' or char == '<blank>' or char == '<unk>':
            temp = ' '.join([char, str(len(buffer))])
            buffer.append(temp)
            continue

        pin = pypinyin.pinyin(char, style=pypinyin.Style.NORMAL, neutral_tone_with_five=True)
        pin = pin[0][0]
        if pin not in seen:
            temp = ' '.join([pin, str(len(buffer))])
            buffer.append(temp.upper())
            seen.add(pin)
        # print(pred)        

with open(write_file_name,'w') as ef:
    buffer = '\n'.join(buffer)
    ef.write(buffer)
