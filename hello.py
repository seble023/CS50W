class flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passengers(self, name):
        if not self.availability():
            return False
        self.passengers.append(name)
        return True

    def availability(self):
        return self.capacity - len(self.passengers)
    

Flight = flight(2)

persons = ["Steven", "kriek", "morrie"]

for people in persons:
    success = Flight.add_passengers(people)
    if success:
        print(f"{people} added")
    else:
        print(f"{people} not added")
    


    

def f(person):
    return person["name"]

people.sort(key=f)
        
        

