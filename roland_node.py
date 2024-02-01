
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

