class Person:
    def __init__(self, me, preferences):
        self.me = me
        self.preferences = preferences #hashmap person to rating
    def get_hatred(self, person):
        if person.me in self.preferences:
            #print(self.me + person.me + str(self.preferences.index(person.me)))
            return self.preferences.index(person.me)**2
        return 0
    def swap(self, person):
        person.me, self.me = self.me, person.me
        person.preferences, self.preferences = self.preferences, person.preferences
