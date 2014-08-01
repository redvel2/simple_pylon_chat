from hw.model.person import Person
from hw.lib.base import Session
import time
def create_generator():
    last_activity=int(time.time())-600
    pers=Session.query(Person).filter(Person.last_activity<last_activity, Person.chanel_id>1).all()
    for i in pers:
        yield i
def main():
    generator=create_generator()
    i=0
    for person in generator:
        i+=1
        person.chanel_id=1
        Session.add(person)
        if i==50:
            Session.commit()
            i=0
    if i!=0:
        Session.commit()
if __name__=='__main__':
    main()