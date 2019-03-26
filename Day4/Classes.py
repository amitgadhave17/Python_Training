from datetime import date
class Person:
    def __init__(self, name, surname, birthdate, email, address, mob, tel):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.email = email
        self.address = address
        self.mob = mob 
        self.tel = tel
        return
    def cal_age(self):
        d2 = date.today()
        d3 =  d2.year - self.birthdate.year
        return d3 
        
    def __del__(self):
        print('deleted'+ str(self.birthdate.year))
        return

if True:
    P = Person('amit', 'gadhave', date(1995,10,17), 'amitgadhave17', 'Pune', '9890', '020')
    P1 = Person('amit', 'gadhave', date(1996,10,17), 'amitgadhave17', 'Pune', '9890', '020')
    P2 = Person('amit', 'gadhave', date(1997,10,17), 'amitgadhave17', 'Pune', '9890', '020')
    print(P.cal_age())
    print(P1.cal_age())
    print(P2.cal_age())
    del P2
print('done')