
from opps.inheritance.single.BaseEx import Base


class Derived(Base):


    def commit(self):
        print("Derived Class Method")
    
    def profiles(self):
        print("Profiles")



d=Derived()
d.Save()
d.Update()
d.commit()