from pybedtools import BedTool
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('target_path')

def bedtoolIntersect(gene_file, tad_order_file, output_file):
    '''
        Use bedtools intersect to find which TADs contain at least 90% of a gene's promoter or at least 90% of an enhancer
    '''
    gene_file_bedtoolFile = BedTool(gene_file)
    tad_order_file_bedtoolFile = BedTool(tad_order_file)

    intersection = gene_file_bedtoolFile.intersect(tad_order_file_bedtoolFile, wa=True, wb=True, f=0.9)
    out = open(output_file, 'w')
    for elt in intersection:
        out.write(str(elt))
    out.close()

if __name__ == "__main__":

    args = parser.parse_args()
    target_path = args.target_path
    os.makedirs(target_path, exist_ok=True)

    bedtoolIntersect('tad/TSSgenesbed', os.path.join(target_path, 'bTADorder'), os.path.join(target_path, 'TSSbTAD'))
    bedtoolIntersect('tad/TSSgenesbed', os.path.join(target_path, 'tTADorder'), os.path.join(target_path, 'TSStTAD'))

    bedtoolIntersect('CREbedDBenhancers_10092018', os.path.join(target_path, 'bTADorder'), os.path.join(target_path, 'enhancersbTAD'))
    bedtoolIntersect('CREbedDBenhancers_10092018', os.path.join(target_path, 'tTADorder'), os.path.join(target_path, 'enhancerstTAD'))