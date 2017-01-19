people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson',
          'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.lstrip("Dr. ")

map(split_title_and_name, people)



filter(lambda person: person.lstrip("Dr. "),people)
map(lambda person: person.lstrip("Dr. "),people)
