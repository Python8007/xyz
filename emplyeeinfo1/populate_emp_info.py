import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','emplyeeinfo1.settings')
import django
django.setup()

from testapp.models import Employee
from faker import Faker
from random import randint
fake=Faker()
def phonenumber():
    num=randint(7,9)
    for i in range(9):
        num=str(num)+str(randint(0,9))
    return int(num)


def populate(n):
    for i in range(1,n+1):
        j=i
        feno=j
        fname=fake.name()
        fphno=phonenumber()
        fsal=fake.random.randint(10000,60000)
        faddr=fake.city()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fname,ephno=fphno,esal=fsal,eadd=faddr)
        j=i+1


populate(50)
# phonenumber()