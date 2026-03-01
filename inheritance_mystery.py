class Arya:
    def a(self):
        print("Arya-a")
    def b(self):
        print("Arya-b")

    def __str__(self):
        return "Arya"

class Oberyn(Arya):
    def b(self):
        print("Oberyn-b")
        super().b()
        self.a()
    def __str__(self):
        return "Oberyn"

class Brienne(Oberyn):
    def a(self):
        print("Brienne-a")

class Tyrion(Arya):
    def a(self):
        super().a()
        print("Tyrion-a")

def main():
    thrones = [Oberyn(), Arya(), Brienne(), Tyrion()]
    #for each of the object above show the results of their behaviors
    for i in range(len(thrones)):
        print('Element', i)
        thrones[i].a()          #call the a method
        print()
        print(thrones[i])       #uses __str__
        print()
        thrones[i].b()          #call the b method
        print('Done')
        print()

main()       
