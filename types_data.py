
class Family:
    def __init__(self, person, position, organization, salary, birth_date, years_old= 0,ratio=0):
        self.person = person
        self.position = position
        self.organization = organization
        self.salary = salary
        self.birth_date = birth_date
        self.years_old = years_old
        self.ratio = ratio

class Price:
    def __init__(self, unit_price, quantity):
        self.unit_price = unit_price
        self.quantity = quantity