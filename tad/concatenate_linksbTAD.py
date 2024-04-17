import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('target_path')

def concatenate(input_files, output_file):
    '''
        makes a combined file for all tissues
    '''
    with open(output_file, 'wb') as outfile:
        for file_name in input_files:
            with open(file_name, 'rb') as infile:
                for line in infile:
                    outfile.write(line)

if __name__ == "__main__":

    args = parser.parse_args()
    target_path = args.target_path
    os.makedirs(target_path, exist_ok=True)

    chromosomes = ['chr' + str(x) for x in range(1, 23)]
    chromosomes.append('chrX')
    chromosomes.append('chrY')
    linkbTAD_list = []

    for chr in chromosomes:
        linkbTAD_list.append(os.path.join(target_path, chr+'linksbTAD'))

    concatenate(linkbTAD_list, os.path.join(target_path, 'linksbTAD'))