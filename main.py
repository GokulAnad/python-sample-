class Myclass:
    year=2020
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        print(self.name,self.age,self.place)
    def addage(self):
        self.age=self.age+1

    def relocated(self,replace):
        self.place=replace
    def display(self):
        print(self.name,self.age,self.place,Myclass.year)
    @classmethod
    def addyear(cls):
        cls.year=cls.year+1
    @staticmethod
    def home():
        print("welcome")



Myclass.home()
x=Myclass("manu",25,"palode")

Myclass.addyear()
x.addage()
x.relocated("ndd")
x.display()



