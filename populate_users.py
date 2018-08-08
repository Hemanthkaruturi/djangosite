import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django

django.setup()

##Fake pop script
import random
from firstapp.models import Users
from faker import Faker

fakegen = Faker()

def populate(N=5):

	for n in range(N):

		fake_first = fakegen.first_name()
		fake_last = fakegen.last_name()
		fake_email = fakegen.email()

		usrs = Users.objects.get_or_create(First_name=fake_first, Last_name=fake_last, email=fake_email)[0]


if __name__ == '__main__':
	print('Populating....')
	populate(20)
	print('Populating completed!')
else:
	print('what the heck!')