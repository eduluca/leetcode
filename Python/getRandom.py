'''
Design a class:
1.) Inserting a value (no duplicates)
2.) Removing a value
3.) getRandom a value that is already inserted (with equal probability)
'''




#removing value from array would be O(n) since we would have to find this value
#removing and insertoing value from hashmap would be O(1)
#random.choice(list) gives random value with equal probability
#hashset would not allow duplicates, it would just replace it or not put it in


class store:
    def __init__(self):
        self.values = []
        self.map = {}
        #self.map = collections.defaultdict(list)

    def insert(self, value):
        if value in self.map:
            return 
        
        self.values.append(values)
        self.map[value] = len(self.values) - 1
        #self.map.add(value) #O(1)

    def remove(self, value):
        if value not in self.map:
            return
        index = self.map[value]

        #Swapping
        last_value = self.values[-1]
        self.values[-1] = value
        self.values[index] = last_value
        self.map[last_value] = index

        self.values.pop()
        del self.map[value]


        #self.map.remove(value) #O(1)

    def get_random():
        #return random.choice(list(self.map)) #O(n)
        return random.choice(self.values)
    



'''
[3,4,4,5,(del)3,random]
self.values = [5,4]
self.map = {4:1,5:0}

Index = 0
Last_val = 5


'''


