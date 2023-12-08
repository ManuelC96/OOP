class Parent:
    def __init__(self, att1, att2):
        self.att1 = att1
        self.att2 = att2
        self.attA = None

    

class Component:
    def __init__(self, attA):
        self.attA = attA
    
    def __str__(self):
        return self.attA

var1 = Parent('Attribute-1', 'Attribute-2')
print(var1.attA)
var1.attA = Component('This is component attribute')
print(var1.attA)



