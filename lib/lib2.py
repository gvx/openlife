import lib1


class Person(lib1.Daemon):
    def __init__(self, chan):
        lib1.Daemon.__init__(self, chan)
        self.age = 0
        self.gender = random.choice((Male, Female))
        if not firstname:
            firstname = 'John' if self.gender == Male else 'Jane'
        if not lastname: lastname = 'Doe'
        self.name = [firstname, lastname]
        self.node = None
    def __call__(self):
        """Subclass at least this function"""
        raise NotImplementedError("__call__ should be subclassed.")
    def __str__(self):
        return 'Person(%s, %s, %s, %s)' % (self.name[0], self.name[1], self.age, self.gender)


class Gender:
    def __init__(self, name):
        self.__doc__ = name
    def __repr__(self):
        return "Gender('" + self.__doc__ + "')"
    def __str__(self):
        return self.__doc__
    def __eq__(self, other):
        return self.__doc__ == other.__doc__

Male = Gender('Male')
Female = Gender('Female')


__all__ = [Person, Male, Female]