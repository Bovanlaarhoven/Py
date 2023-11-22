from faker import Faker

fake = Faker()
username = fake.user_name()
print(username)