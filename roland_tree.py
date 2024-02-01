
import pickle

from roland_node import RolandNode

class RolandTree:
    def __init__(self, items: list):
        self.root = RolandNode(self)
        self.root.value = items[0]
        self.root.append_remainders(items[1:])

        self._savefile = None
    
    @property
    def savefile(self):
        return self._savefile
    
    @savefile.setter
    def savefile(self, savefile_new):
        ext = savefile_new.split('.')[1]
        if ext != 'npy':
            raise Exception('Please have the file extension be \'.npy\'')
        self._savefile = savefile_new
    
    def query_sort(self):
        self.root.sort()
    
    def sorting(self):
        items = self.root.flatten()
        return items

    def save(self):
        file = open(self.savefile, 'wb')
        pickle.dump(self, file)