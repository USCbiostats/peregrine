import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('target_path')

def split(file, target_path):
    '''
        splits input file by chromosome and creates 25 chromosome specific files
    '''
    chromosomes = ['chr' + str(x) for x in range(1, 23)]
    chromosomes.append('chrX')
    chromosomes.append('chrY')

    tad_file = open(file, 'r')
    tad_lines = tad_file.readlines()
    tad_file.close()

    file = os.path.basename(file)
    output_files = {chromosome: open(os.path.join(target_path, chromosome + file), 'w') for chromosome in chromosomes}

    for line in tad_lines:
        chr = line.strip().split('\t')[0]

        if chr in chromosomes:
            output_files[chr].write(line)

    for output_file in output_files.values():
        output_file.close()


if __name__ == "__main__":

    args = parser.parse_args()
    target_path = args.target_path
    os.makedirs(target_path, exist_ok=True)

    split(os.path.join(target_path, 'TSSbTAD'), target_path)
    split(os.path.join(target_path, 'enhancersbTAD'), target_path)