# 1
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self):
        print('speed increased')

    def break_speed(self):
        print('speed breaked')

    def mileage_info(self):
        print(f'mileage of that auto is {self.mileage} miles')


# 2
class Bus(Vehicle):

    def __init__(self, max_speed, mileage, seating_capacity):
        super(Bus, self).__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity


# 3
if issubclass(Bus, Vehicle): print('Class <Bus> is a part of class <Vehicle>')

# 4
school_bus = Bus(110, 2000, 20)

if isinstance(school_bus, Bus):
    print('Variable <school_bus> is object of class <Bus>')
if isinstance(school_bus, Vehicle):
    print('Variable <school_bus> is object of class <Vehicle>')


# 5
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

        def school_adress(self):
            print('What is adress of school?')

        def main_subject(self):
            print('What is main subject?')


class SchoolBus(School, Bus):
    def __init__(self, max_speed, mileage, seating_capacity, get_school_id, number_of_students, bus_school_color):
        super(SchoolBus, self).__init__(get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        self.bus_school_color = bus_school_color

    def Bus_information(self):
        print(f'\nThis is a bus of school #{self.get_school_id}. His max speed is {self.max_speed} '
              f'mileage is {self.mileage}, seatinig capacity is {self.seating_capacity} '
              f'and color is {self.bus_school_color}. A bus carries {self.number_of_students} '
              f'students every day \n')

    def bus_school_col(self):
        print (f'\n Color of bus is {self.bus_school_color}')

    def seating_cap(self):
        print(f'\n Seating capacity of bus is {self.seating_capacity}')


# 6
bus1 = SchoolBus(100, 2000, 20, 1, 10, 'yellow')
bus1.Bus_information()
bus1.bus_school_col()
bus1.seating_cap()


# 7
class Bear:
    def __init__(self, name, meat):
        self.name = name
        self.meat = meat

    def eat(self):
        print(f'Hello. I am a bear. My name is {self.name}. I like {self.meat}')


class Wolf:
    def __init__(self, name, meat):
        self.name = name
        self.meat = meat

    def eat(self):
        print(f'Hello. I am a wolf. My name is {self.name}. I like {self.meat}')


Bear1 = Bear('Brown', 'fish')
Wolf1 = Wolf('Gray', 'rabbit \n')

for wild in (Bear1, Wolf1):
    wild.eat()


# 8
class City():
    def __new__(cls, name, population):
        if population > 1500:
            obj = super().__new__(cls)
            obj.name = name
            obj.population = population
            print(f'Population of {name} is {population}')
            return obj
        else:
            print(f'Your city {name} is too small')


    def __init__(self, name, population):
        self.name = name
        self.population = population


NY = City('New York', 2000)
LV = City('Las Vegas', 1499)

print(NY)
print(LV)
