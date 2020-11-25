'''
Required Features:
- [x] Create a class called AnimalShelter which holds only dogs and cats.
- [x] The shelter operates using a first-in, first-out approach.
- [x] Implement the following methods:
- [x] enqueue(animal): adds animal to the shelter.
- [x] animal can be either a dog or a cat object.
- [x] dequeue(pref): returns either a dog or a cat.
- [x] If pref is not "dog" or "cat" then return null.
- [x] Stretch: If a cat or dog isn’t preferred, return whichever animal has been waiting in the shelter the longest.
'''

from stacks_and_queues.stacks_and_queues import Queue, InvalidOperationError

class AnimalShelter():
    def __init__(self):
        self.cat_queue = Queue()
        self.dog_queue = Queue()
        self.animals_served = 0

    def enqueue(self, incoming_animal):
        type_of_animal = type(incoming_animal)
        # https://docs.python.org/3/library/functions.html#type
        self.animals_served += 1
        incoming_animal.animal_id = self.animals_served
        if type_of_animal == Cat:
            self.cat_queue.enqueue(incoming_animal)
        elif type_of_animal == Dog:
            self.dog_queue.enqueue(incoming_animal)
        else:
            raise InvalidOperationError("Sorry, we don't accept that type of animal here.")

    def dequeue(self, request_type = None):
        if request_type == "cat":
            return self.cat_queue.dequeue()
        elif request_type == "dog":
            return self.dog_queue.dequeue()
        elif request_type == None:
            #which queue is older?
            next_cat = self.cat_queue.peek().animal_id
            next_dog = self.dog_queue.peek().animal_id
            if next_cat < next_dog:
                return self.cat_queue.dequeue()
            else:
                return self.dog_queue.dequeue()
        else:
            return None

class Animal():
    def __init__(self, name=None):
        self.adoptable = True
        self.trait = "cute"
        self.name = name

class Cat(Animal):
    pass

class Dog(Animal):
    pass
