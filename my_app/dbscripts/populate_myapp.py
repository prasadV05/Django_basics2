'''
python manage.py shell
execute the below command inside the shell
exec(open('./my_app/dbscripts/populate_my_app.py').read())'''

from faker import Faker
from my_app.models import My_app
MAX_LIMIT=1000
AGES= [i for i in range(1,99)]
fake= Faker()

class PopulateMyapp:
    def __init__(self) -> None:
        pass

    def fetch_random_age(self):
        return fake.random_choices(elements=AGES, length=1)
    def run(self):
        for i in range(1,MAX_LIMIT):
            name=fake.name()
            age=self.fetch_random_age()[0]
            print("i",i)
            print("name",name)
            print("age",age)
            My_app.objects.create(
                name=name,
                age=age
            )

populate_myapp= PopulateMyapp()
populate_myapp.run()