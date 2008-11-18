#!./stackless-26-export/python
#OpenLife game engine (Python)

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program. If not, see <http://www.gnu.org/licenses/>.

#Version:
Info = dict(ver=(0, 0, 1, 'a'))

if __name__ != '__main__':
    raise ImportError("Not a module: to run the game, use './run'")
    exit(1)

import stackless
import math
import sys
import random
from RenderText import Render
#from Render import Render

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

class Daemon(object):
    """A "process" running in the background, to maintain important things, that are not always visible.

    Meant to be subclassed."""
    def __init__(self, **kwargs):
        self.__dict__ = kwargs
    def __str__(self):
        if 'info' in self.__dict__:
            return self.__dict__['info']
        else:
            return 'DAEMON'

DeamonList = []
ObjectList = []
PersonList = []

def kernel():
    ##print "MAIN"
    renderChan = stackless.channel()
    renderTasklet = stackless.tasklet(runrender)(renderChan)
    stackless.run()
    while True:
        if renderChan.balance > 0:
            msg = renderChan.receive().split()
            try:
                if msg[0] == 'KILL':
                    if msg[1] == '*':
                        for thread in DeamonList + ObjectList + PersonList:
                            thread.kill()
                        renderTasklet.kill()
                        break
                elif msg[0] == 'QUIT':
                    for thread in DeamonList + ObjectList + PersonList:
                        thread.kill()
                    renderTasklet.kill()
                    break
                elif msg[0] == 'SEND':
                    if msg[1] == 'INFO':
                        renderChan.send(Info)
                    elif msg[1] == 'UPDATE':
                        if msg[2] == 'NOW':
                            renderChan.send('Update: nothing happened.')
                        elif msg[2] == 'CHANGES':
                            renderChan.send('Update: nothing happened.')
                        else:
                            renderChan.send('Update: nothing happened.')
                elif msg[0] == 'LOAD':
                    pass #load from msg[1]
                elif msg[0] == 'SAVE':
                    pass #save to msg[1]
            except:
               pass
        stackless.schedule()
    ##print Daemon(p=3, q='z').__dict__
    ##print Daemon(p=3, q='z')
    ##print Daemon(p=3, info='z')
    ##print "END_OF_MAIN"

def runperson(person, chan):
    pass

def runobject(object, chan):
    pass

def rundeamon(deamon, chan):
    pass

def runrender(chan):
    render = Render(chan)
    if render.callonce:
        render()
        #if r == -1: #Quit
        #    return -1
    else:
        while True:
            render()
            stackless.schedule()

def init():
    kernel()

init()