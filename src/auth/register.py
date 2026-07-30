from src.database.insert import insert_user
from src.database.queries import get_user_by_email
from src.auth.password import hash_password

def register_user(username,email,password,role):
    existing_user = get_user_by_email(email)
    if existing_user:
        return False

    #hash the password
    password_hash = hash_password(password)


    insert_user(
            username,
            email,
            password_hash,
            role
            )
    return True
