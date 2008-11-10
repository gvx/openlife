#!./stackless-26-export/python
#OpenLife game engine (Python)
#Version: (see DOCS/VERSION)
ver = (0, 0, 0, 'a')

if __name__ != '__main__':
    raise ImportError("Not a module: to run the game, use './run'")
    exit(1)

import stackless
import math
import sys
import random

class Gender:
    def __init__(self, name):
        self.__doc__ = name
    def __repr__(self):
        return "Gender('" + self.__doc__ + "')"
    def __str__(self):
        return self.__doc__

Male = Gender('Male')
Female = Gender('Female')

class PersonData:
    def __init__(self, person=None):
        if person == None:
            self.age = 0
            self.gender = random.choice((Male, Female))
            firstname = 'John' if gender == Male else 'Jane'
            self.name = [firstname, 'Doe']
        else:
            self.age = person.age
            self.name = person.name
            self.gender = person.gender

class Person:
    """A person, that handles his own actions. Use PersonData in communication for encapsulation
    """
    def __init__(self, firstname=None, lastname=None, age=0, gender=None):
        self.age = age
        if gender == None:
            gender = random.choice((Male, Female))
        if not firstname:
            firstname = 'John' if gender == Male else 'Jane'
        if not lastname: lastname = 'Doe'
        self.name = [firstname, lastname]
        self.gender = gender
        self.node = None
    def __repr__(self):
        return 'Person(%s, %s, %s, %s)' % (self.name[0], self.name[1], self.age, self.gender)
    def data(self):
        """Return PersonData for this Person."""
        return PersonData(self)

class TreeNode:
    def __init__(self, person, parents=None, children=None, spouse=None):
        if parents:
            self.parents = parents
        else:
            self.parents = []
        if children:
            self.children = children
        else:
            self.children = []
        self.spouse = spouse
        self._person = person

class FamilyTree:
    """FamilyTree class -> one object to rule them all"""
    def __init__(self, nodes=None):
        if nodes == None: nodes = []
        self.nodes = nodes
    def makechild(self, parents):
        self.nodes.append(TreeNode(Person(lastname=parents[0].name[1]), parents))
        for parent in parents:
            parent.children.append(self.nodes[-1])
    def marry(self, firstperson, secondperson):
        firstperson.spouse = secondperson
        secondperson.spouse = firstperson
        secondperson.name[1] = firstperson.name[1]

class Object:
    pass

class Deamon(object):
    """A "process" running in the background, to maintain important things, that are not always visible.

    Meant to be subclassed."""
    def __init__(self, **kwargs):
        self.__dict__ = kwargs
    def __str__(self):
        if 'info' in self.__dict__:
            return self.__dict__['info']
        else:
            return 'DEAMON'

def kernel():
    print "MAIN"
    stackless.schedule()
    stackless.schedule()
    print Deamon(p=3, q='z').__dict__
    print Deamon(p=3, q='z')
    print Deamon(p=3, info='z')
    print "END_OF_MAIN"

def printSome(a):
    print "Whoa", a
    stackless.schedule()
    print "Flr", a

def runperson(person, chan):
    pass

def runobject(object, chan):
    pass

def rundeamon(deamon, chan):
    pass

def main():
    stackless.tasklet(kernel)()
    for i in xrange(30):
        stackless.tasklet(printSome)(i)
    stackless.run()

main()