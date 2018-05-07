class HauntedBus:

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)

bus1 = HauntedBus(['A', 'B'])
print(bus1.passengers)
bus1.pick('C')
bus1.drop('A')
print(bus1.passengers)
bus2 = HauntedBus()
bus2.pick('C')
print(bus2.passengers)

# 如果初始化时提供参数，则不会影响，如果不提供，则会共享同一个初始列表
bus3 = HauntedBus()
bus3.pick('D')
print(bus2.passengers)
print(bus2.passengers)


class TwilightBus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)#使用参数的副本
    
    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)
