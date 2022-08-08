class Employee:
    company="Google"
    salary=100
    def getSalary(self):
        print(f"Salary is {self.salary}")
    def greet(self):
        print("Good morning sir")

#jab bhe aap koy bhe functiion bnata ho class ka use kar kar too uska liya huma self use karna padta hai
#bina self k code chalega nahe
#STATIC METHOD USE HOTA HAI FUNCTION CALLING K TIME HUM KO PARAMETER NH DALTA USMA
harry=Employee()
harry.salary=1000
harry.getSalary()

