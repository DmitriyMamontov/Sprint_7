from faker import Faker

fake = Faker()

def generate_new_courier():
    return {
        "login": fake.name(),
        "password": fake.password(length=10),
        "firstName": fake.first_name(),
    }
def generate_new_order():
    return {
    "firstName": fake.name(),
    "lastName": fake.last_name(),
    "address": fake.address(),
    "metroStation": fake.random_int(min=1, max=10),
    "phone": fake.phone_number(),
    "rentTime": fake.random_int(min=1, max=5),
    "deliveryDate": fake.date_between(start_date='today', end_date='+30d').isoformat(),
    "comment": fake.word()
}