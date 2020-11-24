from stacks_and_queues.stacks_and_queues import Queue, InvalidOperationError

class AnimalShelter():
    def __init__(self):
        self.cat_queue = Queue()
        self.dog_queue = Queue()

    def enqueue(self, incoming_animal):
        type_of_animal = type(incoming_animal)
        if type_of_animal == Cat:
            self.cat_queue.enqueue(incoming_animal)
        elif type_of_animal == Dog:
            self.dog_queue.enqueue(incoming_animal)
        else:
            raise InvalidOperationError("Sorry, we don't accept that type of animal here.")

class Animal():
    def __init__(self, name=None):
        self.adoptable = True
        self.trait = "cute"
        self.name = name

class Cat(Animal):
    pass

class Dog(Animal):
    pass
