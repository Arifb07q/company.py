class Employee:
    raise_amt = 2.05
    def _init_(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
class Developer(Employee):
    raise_amt = 1.10
    def _init_(self, first, last, pay, prog_lang):
        super()._init_(first, last, pay)
        self.prog_lang = prog_lang
class Manager(Employee):
    def _init_(self, first, last, pay, employees=None):
        super()._init_(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
dev_1 = Developer('Murat', 'Can', 50000, 'Python')
dev_2 = Developer('Arif', 'bzky', 60000, 'Java')
mgr_1 = Manager('Piotr', 'Smith', 90000, [dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)
mgr_1.print_emps()