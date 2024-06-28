import random
class RandomizedSet(object):

    def __init__(self):
        self.hashmap = {}
        self.list_of_vals = []

    def insert(self, val):
        statement = val not in self.hashmap
        if statement:
            self.hashmap[val] = len(self.list_of_vals)
            self.list_of_vals.append(val)
        return statement

        
    def remove(self, val):
        statement = val in self.hashmap
        if statement:
            self.hashmap[self.list_of_vals[-1]] = self.hashmap[val]
            del self.hashmap[val]

            self.list_of_vals[self.hashmap[self.list_of_vals[-1]]] = self.list_of_vals[-1]
            self.list_of_vals.pop(-1)
            

        return statement

    def getRandom(self):
        return self.list_of_vals[random.randint(0, len(self.list_of_vals)-1)]

if __name__ == '__main__':
    rset = RandomizedSet()
    print(rset.insert(1))
    print(rset.insert(2))
    print(rset.insert(3))
    print(rset.insert(5))
    print(rset.insert(7))
    print(rset.insert(0))
    print(rset.remove(1))
    print(rset.getRandom())