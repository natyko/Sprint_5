import random


# Generate random email
def generate_random_email():
    name = "testuser"
    cohort = random.randint(10, 99)
    unique_number = random.randint(100, 999)
    domain = "yandex.ru"
    return f"{name}_{cohort}_{unique_number}@{domain}"
