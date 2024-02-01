
from pathlib import Path
import argparse
import pickle

class RolandNode:

    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None

    def sort(self, alternates):
        if alternates:
            self.less = []
            self.more = []
            for item in alternates:
                print(f'{self.value} (1) VS {item} (2)')
                selected = False
                while not selected:
                    keypress = input('')
                    if not keypress.isdigit():
                        print('Please type in a digit')
                        continue
                    keypress = int(keypress)
                    if keypress == 1:
                        # Need to save?
                        self.less.append(item)
                        selected = True
                    elif keypress == 2:
                        # Need to save?
                        self.more.append(item)
                        selected = True
                    else:
                        print('Please enter a value (1 or 2)')
            if self.less:
                self.left = RolandNode(self.less[0])
                self.left.sort(self.less[1:])
            if self.more:
                self.right = RolandNode(self.more[0])
                self.right.sort(self.more[1:])

    def flatten(self) -> list:
        output = []
        if self.left:
            values_left = self.left.flatten()
            output.extend(values_left)
        output.append(self.value)
        if self.right:
            values_right = self.right.flatten()
            output.extend(values_right)
        return output


class RolandTree:
    def __init__(self, items: list):
        self.root = RolandNode(items[0])
        self.remainders = items[1:]
    
    def query_sort(self):
        self.root.sort(self.remainders)
    
    def __str__(self):
        print(self.root)
    
    def sorting(self):
        items = self.root.flatten()
        return items


def main(args):
    file_path = Path(args.filename)
    extension = file_path.suffix
    file = file_path.open()
    if extension == '.txt':
        items = []
        for line in file.readlines():
            items.append(line.strip())
        tree = RolandTree(items)
    elif extension == '.npy':
        tree = pickle.load(file)
    else:
        raise Exception(f'Unrecognised file extension: {extension}')
    tree.query_sort()
    items_sorted = tree.sorting()
    items_sorted.reverse()
    for i, item in enumerate(items_sorted):
        print(f'{i+1}: {item}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='roland_sort.py',
                    description='Sort via bubble sort + saving',
                    epilog='Vytenis :)')
    parser.add_argument('filename')
    args = parser.parse_args()
    main(args)