import random
from typing import List

from faker import Faker


# Валидные поля fullname, email, current address, permanent address
def g_get_valid_fields() -> List[List]:
    fake = Faker()
    lst = []

    for i in range(5):
        lst.append([fake.name(), fake.email(), fake.address(), fake.secondary_address()])

    return lst


# Невалидное поле email
def g_get_invalid_email():
    allowed_chars = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    longer_email = f"{"".join(random.choice(allowed_chars) for _ in range(1000))}@example.com"

    spec_symbol = ",!@#$%^&"
    spec_symbol_lst = []

    for i in spec_symbol:
        spec_symbol_lst.append(f"example{i}@gmail.com")

    lst = ["test_example.com", "", longer_email, random.choice(spec_symbol_lst), "<script>alert('xss')</script>",
           "1' OR '1'='1", ":):):):))))::;)", "<div>HTML injection</div>"]
    return lst
