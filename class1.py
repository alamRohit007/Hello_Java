
class RailwayForm:
    type="RailwayForm"
    def printType(self):
        print(f"The name is {self.name}")
        print(f"The name is {self.age}")
        
k=RailwayForm()
k.name='Rohit'
k.age=25

k.printType()