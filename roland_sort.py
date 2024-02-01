
from pathlib import Path
import argparse
import pickle
import datetime

from roland_tree import RolandTree

def main(args):
    file_path = Path(args.filename)
    extension = file_path.suffix

    # Handle loading in save destination
    if not args.savefile:
        presentDate = datetime.datetime.now()
        unix_timestamp = datetime.datetime.timestamp(presentDate)*1000
        namebody = str(int(unix_timestamp))
        savefile = namebody + '.npy'
    else:
        savefile = args.savefile

    # Load either item file or savefile
    if extension == '.txt':
        items = []
        file = file_path.open()
        for line in file.readlines():
            items.append(line.strip())
        tree = RolandTree(items)
        tree.savefile = savefile
    elif extension == '.npy':
        file = open(file_path, 'rb')
        tree = pickle.load(file)
        tree.savefile = savefile
    else:
        raise Exception(f'Unrecognised file extension: {extension}')

    tree.query_sort()
    items_sorted = tree.sorting()
    items_sorted.reverse()
    output = ''
    for i, item in enumerate(items_sorted):
        output += f'{i+1}: {item}\n'
    print('Results!')
    print(output)
    result_filename = tree.savefile.split('.')[0]
    result_filename += '_results.txt'
    resultfile = open(result_filename, 'w')
    resultfile.write(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='roland_sort.py',
                    description='Sort via bubble sort + saving',
                    epilog='Vytenis :)')
    parser.add_argument('filename')
    parser.add_argument(
        '-s', '--savefile',
        help='The file to where the save the intermediate values') 
    args = parser.parse_args()
    main(args)