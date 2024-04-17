from math import floor, ceil
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('target_path')

def bTADoverlap(input_file, output_file, cell_type):
    tad_file = open(input_file, 'r')
    tad_lines = tad_file.readlines()
    tad_file.close()

    hash = {}
    for line in tad_lines:
        chr, start1, end1, location, pval = line.strip().split('\t')
        score = pval + '|' + cell_type
        location_split = location.split('___')
        one = location_split[0]
        two = location_split[1]
        three = one.split('|')[2]
        four = two.split('|')[2]
        five = three.split(':')[1]
        six = four.split(':')[1]
        s1, s2 = five.split('-')
        e1, e2 = six.split('-')
        start = floor((int(s1) + int(s2))/2)
        end = ceil((int(e1) + int(e2))/2)
        total = f"{chr}\t{start}\t{end}\t{location}\t{score}"
        hash[total] = 1

    out = open(output_file, 'w')
    for key in sorted(hash.keys()):
        out.write(key + '\n')
    out.close()

def tTADOverlap(input_file, output_file, cell_type):
    tad_file = open(input_file, 'r')
    tad_lines = tad_file.readlines()
    tad_file.close()

    out = open(output_file, 'w')

    for line in tad_lines:
        chr, start, end, location, pval = line.strip().split('\t')
        score = pval + '|' + cell_type
        out.write(f"{chr}\t{start}\t{end}\t{location}\t{score}\n")
    out.close()


if __name__ == "__main__":

    args = parser.parse_args()
    target_path = args.target_path
    os.makedirs(target_path, exist_ok=True)

    bTADoverlap('tad/ENCFF274VJU.bed', os.path.join(target_path, 'bTADorder'), 'Caki2')
    tTADOverlap('tad/ENCFF588KUZ.bed', os.path.join(target_path, 'tTADorder'), 'Caki2')