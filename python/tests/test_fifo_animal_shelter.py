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
