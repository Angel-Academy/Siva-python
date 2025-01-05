'''
name="ravikumar"
print(len(name))
d={"name":"siva",
   "age":10,
   "gender":"male",
   "country":"india"}
print(len(d))
'''
class transport:
    def __init__(self):
        print("transportation")
    def ways(self):
        print("many ways")
    def trade(self):
        print("impot and export")
class car(transport):
    def ways(self):
        print("road ways")
class ship(transport):
    def ways(self):
        print("sea ways")
class areoplane(ship,transport):
    def ways(self):
        print("air ways")
    def print(self):
        self.ways()
        ship.ways(self)
        super().trade()

vechile=transport()
audi=car()
tayoto=ship()
airindia=areoplane()
audi.ways()
airindia.print()
airindia.trade()
