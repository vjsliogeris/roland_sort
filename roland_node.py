
class RolandNode:
    def __init__(self, caller):
        self.superitem = caller
        self._value = None # The value of this node
        self.remainders = [] # Unsorted items in this nodes' bucket
        self.left = None
        self.right = None
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_val):
        ''' Populate current node

        Creates child nodes since this node is nonempty
        '''
        self._value = new_val
        self.left = RolandNode(self)
        self.right = RolandNode(self)
    
    def append_remainders(self, values: list):
        if not self.value:
            self.value = values.pop(0)
        self.remainders.extend(values)

    def __handle_remainder(self):
        print(f'{len(self.remainders)} remaining for {self.value}')
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
                self.left.append_remainders([item])
                selected = True

            elif keypress == 2:
                self.right.append_remainders([item])
                selected = True
            else:
                print('Please enter a value (1 or 2)')
        self.save()

    def sort(self):
        while self.remainders:
            self.__handle_remainder()
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