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

        l = line.split('\t')
        if len(l) < 2:
            continue
        filename, text = l
        
        buffer.append(text)
        

with open(write_file_name,'w') as ef:
    buffer = '\n'.join(buffer)
    ef.write(buffer)
