from app.utils.hash import get_password_hash, verify_password
from faker import Faker

fake = Faker()

def test_get_password_hash():
    password = fake.password()
    hashed_password = get_password_hash(password)

    assert hashed_password != password



def test_verify_correct_password():
    password = fake.password()
    hashed_password = get_password_hash(password)
    is_same_password = verify_password(password, hashed_password)

    assert is_same_password == True


def test_verify_incorrect_password():
    password = fake.password()
    hashed_password = get_password_hash(password)
    other_password = fake.password()
    is_same_password = verify_password(other_password, hashed_password)

    assert is_same_password == False
