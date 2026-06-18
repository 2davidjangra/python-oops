class Employee:

    def work(self):
        print("Employee Working")

class Manager(Employee):

    def manage(self):
        print("Managing Team")

m1 = Manager()

m1.work()
m1.manage()
