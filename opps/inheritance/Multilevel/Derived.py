
from DrivedBase import DerivedBase


class Derived(DerivedBase):


    def School(self):
        print("Derived School")
    
    def collage(self):
        print("Derived Collage")


d= Derived()
d.save()
d.Amount()
d.collage()