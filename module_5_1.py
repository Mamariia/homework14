class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):

        if new_floor <= self.number_of_floors and new_floor > 0:
            a = 1
            while a <= new_floor:
                print(a)
                a += 1
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Клевер', 11)
h2 = House('ЖК Литературный', 6)
h1.go_to(8)
h2.go_to(10)