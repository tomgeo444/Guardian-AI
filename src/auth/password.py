import bcrypt


def hash_password(password):
    """
    Takes a plain-text password and returns a bcrypt hash.
    Used during user registration.
    """

    # Convert the password string into bytes because bcrypt only works with bytes.
    password_bytes = password.encode("utf-8")

    # Generate a random salt.
    # The salt makes identical passwords produce different hashes.
    salt = bcrypt.gensalt()

    # Hash the password using the generated salt.
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    # Convert the hash back to a normal string so it can be stored in MariaDB.
    return hashed_password.decode("utf-8")


def verify_password(password, stored_hash):
    """
    Checks whether the entered password matches the stored bcrypt hash.
    Used during user login.
    """

    # Convert the entered password into bytes.
    password_bytes = password.encode("utf-8")

    # Convert the stored hash from the database into bytes.
    stored_hash_bytes = stored_hash.encode("utf-8")

    # bcrypt.checkpw() automatically:
    # 1. Extracts the salt from the stored hash.
    # 2. Hashes the entered password using that salt.
    # 3. Compares the newly generated hash with the stored hash.
    # Returns:
    #   True  -> Password is correct.
    #   False -> Password is incorrect.
    return bcrypt.checkpw(password_bytes, stored_hash_bytes)
