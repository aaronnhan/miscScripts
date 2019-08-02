from person import Person
from group import Group
my_list = []
NUM_GROUPS = 2
groups = []

with open("people.txt", "r") as f:
    for x in f:
        info = x.split()
        my_list.append(Person(info[0], info[1::]))
#Generates preliminary groups
num_people = len(my_list)
person_index = 0
for x in range(NUM_GROUPS):
    current_group = []
    if num_people%NUM_GROUPS == 0:
        for y in range(len(my_list)//NUM_GROUPS):
            current_group.append(my_list[person_index])
            person_index+=1
    else:
        for y in range(len(my_list)/NUM_GROUPS + 1):
            current_group.append(my_list[person_index])
            person_index+=1
    groups.append(Group(current_group))
def swap(groups):
    continue_swapping = False
    for group in groups:
        for other_group in groups:
            if group != other_group:
                for person in group.my_people:
                    for other_person in other_group.my_people:
                        before_hatred = group.get_hatred() + other_group.get_hatred()
                        person.swap(other_person)
                        after_hatred = group.get_hatred() + other_group.get_hatred()
                        if  after_hatred >= before_hatred:
                            person.swap(other_person)
                        else:
                            continue_swapping = True
    if continue_swapping:
        swap(groups)

swap(groups)

for group in groups:
    for person in group.my_people:
        print(person.me)
    print("\n")
