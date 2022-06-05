class Myclass:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        print(self.name,self.age,self.place)
    def addage(self):
        self.age=self.age+1
        print(self.age)
    def relocated(self,replace):
        self.place=replace
        print(self.place)



x=Myclass("manu",25,"palode")
x.addage()
x.relocated("ndd")


