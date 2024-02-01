
from pathlib import Path
import argparse
import pickle
import datetime

class RolandNode:

    def __init__(self, caller):
        self.superitem = caller
        self.value = None # The value of this node
        self.remainders = [] # Unsorted items in this nodes' bucket
        self.left = None
        self.right = None
    
    def add_value(self, value):
        ''' Populate current node

        Creates child nodes since this node is nonempty
        '''
        self.value = value
        self.left = RolandNode(self)
        self.right = RolandNode(self)
    
    def append_remainders(self, values: list):
        if not self.value:
            self.value = values[0]
            self.left = RolandNode(self)
            self.right = RolandNode(self)
        else:
            self.remainders.extend(values)

    def sort(self):
        print(f'!!! Sorting {self.value}')
        while self.remainders:
            item = self.remainders.pop()
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
                    self.left.append_remainders([item])
                    selected = True

                elif keypress == 2:
                    # Need to save?
                    self.right.append_remainders([item])
                    selected = True
                else:
                    print('Please enter a value (1 or 2)')
            self.save()
        if self.left:
            self.left.sort()
        if self.right:
            self.right.sort()

    def flatten(self) -> list:
        output = []
        if self.left:
            values_left = self.left.flatten()
            output.extend(values_left)
        if self.value:
            output.append(self.value)
        if self.right:
            values_right = self.right.flatten()
            output.extend(values_right)
        return output


    def save(self):
        self.superitem.save()


class RolandTree:
    def __init__(self, items: list):
        self.root = RolandNode(self)
        self.root.add_value(items[0])
        self.root.append_remainders(items[1:])
    
    def query_sort(self):
        self.root.sort()
    
    def __str__(self):
        print(self.root)
    
    def sorting(self):
        items = self.root.flatten()
        return items

    def save(self):
        savefolder = Path('intermediates/')
        if not savefolder.exists():
            savefolder.mkdir()
        presentDate = datetime.datetime.now()
        unix_timestamp = datetime.datetime.timestamp(presentDate)*1000
        namebody = str(int(unix_timestamp))
        filename = 'intermediates/' + namebody + '.npy'
        file = open(filename, 'wb')
        pickle.dump(self, file)



def main(args):
    file_path = Path(args.filename)
    extension = file_path.suffix
    if extension == '.txt':
        items = []
        file = file_path.open()
        for line in file.readlines():
            items.append(line.strip())
        tree = RolandTree(items)
    elif extension == '.npy':
        file = open(file_path, 'rb')
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