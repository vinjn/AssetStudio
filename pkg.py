import csv
import json
import datetime
from pathlib import Path
from collections import defaultdict 

def process_pkg_csv(filename):
    dir_name = Path(filename).parent
    print(filename, dir_name)
    with open(filename, encoding='utf-8') as infile:
        if 'tsv' in filename:
            reader = csv.DictReader(infile, delimiter='\t')
        else:
            reader = csv.DictReader(infile)
        for row in reader:
            # print(row)
            file_path = dir_name / row['FileName']
            print(row['Name'], file_path.stat().st_size)

process_pkg_csv('d:/t3-202105120931fc9190.1620783875/test2/pkg.csv')