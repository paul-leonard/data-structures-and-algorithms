'''
Required Tests:
- [x] “Happy Path” - Expected outcome
- [x] Expected failure
- [x] Edge Case (if applicable/obvious)
'''

import pytest

from code_challenges.fifo_animal_shelter.fifo_animal_shelter import Cat, Dog, Animal, AnimalShelter
from stacks_and_queues.stacks_and_queues import Queue, InvalidOperationError

# py project .toml lives... that is the route directory....

def test_connection():
    return AnimalShelter()

def test_animal_is_cute():
    animal = Animal()
    actual = animal.trait
    expected = "cute"
    assert actual == expected

def test_make_a_cat():
    cat = Cat()
    actual = type(cat)
    expected = Cat
    assert actual == expected

def test_dog_is_cute():
    dog = Dog()
    actual = dog.trait
    expected = "cute"
    assert actual == expected

def test_name():
    dog = Dog("Fido")
    actual = dog.name
    expected = "Fido"
    assert actual == expected

def test_enqueue_cat():
    cat = Cat("Felix")
    shelter = AnimalShelter()
    shelter.enqueue(cat)
    actual = shelter.cat_queue.peek().name
    expected = "Felix"
    assert actual == expected

def test_enqueue_dog():
    dog = Dog("Spot")
    shelter = AnimalShelter()
    shelter.enqueue(dog)
    actual = shelter.dog_queue.peek().name
    expected = "Spot"
    assert actual == expected

def test_request_cat():
    cat = Cat("Felix")
    shelter = AnimalShelter()
    shelter.enqueue(cat)
    actual = shelter.dequeue("cat").name
    expected = "Felix"
    assert actual == expected

def test_request_cat_line_of_two():
    cat = Cat("Felix")
    cat2 = Cat("Garfield")
    shelter = AnimalShelter()
    shelter.enqueue(cat)
    shelter.enqueue(cat2)
    actual = shelter.dequeue("cat").name
    expected = "Felix"
    assert actual == expected

def test_request_cat_line_of_two_second():
    cat = Cat("Felix")
    cat2 = Cat("Garfield")
    shelter = AnimalShelter()
    shelter.enqueue(cat)
    shelter.enqueue(cat2)
    shelter.dequeue("cat")
    actual = shelter.dequeue("cat").name
    expected = "Garfield"
    assert actual == expected

def test_request_dog_line_of_two():
    dog = Dog("Spot")
    dog2 = Dog("Clifford")
    shelter = AnimalShelter()
    shelter.enqueue(dog)
    shelter.enqueue(dog2)
    actual = shelter.dequeue("dog").name
    expected = "Spot"
    assert actual == expected

def test_request_snake():
    cat = Cat("Felix")
    shelter = AnimalShelter()
    shelter.enqueue(cat)
    actual = shelter.dequeue("snake")
    expected = None
    assert actual == expected

def test_request_dog_empty():
    dog = Dog("Spot")
    dog2 = Dog("Clifford")
    shelter = AnimalShelter()
    shelter.enqueue(dog)
    shelter.enqueue(dog2)
    shelter.dequeue("dog")
    shelter.dequeue("dog")
    #context manager (aka bubble) to raise errors in to test them; otherwise seen as legit error.  Thanks Skyler!
    with pytest.raises(InvalidOperationError):
        shelter.dequeue("dog")

def test_animal_id_counter_cat():
    dog = Dog("Spot")
    dog2 = Dog("Clifford")
    cat = Cat("Felix")
    cat2 = Cat("Garfield")
    shelter = AnimalShelter()
    shelter.enqueue(dog)
    shelter.enqueue(dog2)
    shelter.enqueue(cat)
    shelter.enqueue(cat2)
    actual = shelter.cat_queue.peek().animal_id
    expected = 3
    assert actual == expected

def test_animal_id_counter_dog():
    dog = Dog("Spot")
    dog2 = Dog("Clifford")
    cat = Cat("Felix")
    cat2 = Cat("Garfield")
    shelter = AnimalShelter()
    shelter.enqueue(dog)
    shelter.enqueue(dog2)
    shelter.enqueue(cat)
    shelter.enqueue(cat2)
    actual = shelter.dog_queue.peek().animal_id
    expected = 1
    assert actual == expected

def test_waiting_longer_animal():
    dog = Dog("Spot")
    dog2 = Dog("Clifford")
    cat = Cat("Felix")
    cat2 = Cat("Garfield")
    shelter = AnimalShelter()
    shelter.enqueue(dog)
    shelter.enqueue(dog2)
    shelter.enqueue(cat)
    shelter.enqueue(cat2)
    new_pet = shelter.dequeue()
    actual = type(new_pet)
    expected = Dog
    assert actual == expected
