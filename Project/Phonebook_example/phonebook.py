class Phonebook:

    def __init__(self):
        self.entries = {}

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def is_consistent(self):
        keys = []
        values = []
        for key,value in self.entries.items():
            keys.append(key)
            values.append(value)
        if len(keys) == len(list(set(values))):
            return True
        else:
            return False

    def get_names(self):
        return self.entries.keys()

    def get_numbers(self):
        return self.entries.values()
