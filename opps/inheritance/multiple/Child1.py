
from BaseEx import Base


class  Child1(Base):


    def childClass(self):
        print("child 1 Class")




c= Child1()
c.save()
c.childClass()