class Grandfather:
    def __init__(self):
        self.name = "ABC"
        self.inherit = "100000"
        self.purchase = "1000"

class Father(Grandfather):
    def __init__(self):
        super().__init__()
        self.name = " AABB " + self.name
        self.purchase = "2000" + self.purchase

class Child(Father):
    def __init__(self, name):
        super().__init__()
        self.name = name + self.name
        # Fix the line below, assuming you want to keep the existing purchase value.
        self.purchase = self.purchase
        print("Hello", self.name)
        print("Inherited Property: Rs", self.inherit)
        print("Total Property ", self.inherit + self.purchase)

obj = Child("John")


        
        