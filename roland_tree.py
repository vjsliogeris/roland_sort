
import pickle

from roland_node import RolandNode

class RolandTree:
    def __init__(self, items: list):
        self.root = RolandNode(self)
        self.root.add_value(items[0])
        self.root.append_remainders(items[1:])
    
    def add_savefile(self, savefile):
        self.savefile = savefile
        print(savefile)
    
    def query_sort(self):
        self.root.sort()
    
    def __str__(self):
        print(self.root)
    
    def sorting(self):
        items = self.root.flatten()
        return items

    def save(self):
        file = open(self.savefile, 'wb')
        pickle.dump(self, file)


