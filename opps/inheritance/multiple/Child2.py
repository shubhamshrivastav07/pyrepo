from BaseEx import Base


class  Child2(Base):


    def childClass(self):
        print("child 2 Class")



c2= Child2()
c2.save()
c2.childClass()