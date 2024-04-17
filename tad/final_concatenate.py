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

    concatenate([os.path.join(target_path, 'linksbTADtissues'), os.path.join(target_path, 'linkstTADtissues')], os.path.join(target_path, 'linksTADtissues'))