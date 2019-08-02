class Group:
    def __init__(self, people):
        self.my_people = people
    def get_hatred(self):
        hatred = 0;
        for person in self.my_people:
            for other_person in self.my_people:
                if other_person != person:
                    hatred += person.get_hatred(other_person)
        print(hatred)
        return hatred