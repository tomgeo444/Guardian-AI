from src.database.queries import get_user_by_email
from src.auth.password import verify_password


def login_user(email,password):
	user=get_user_by_email(email)
	if not user:
		return False
	#get the stored password hash
	password_hash =user[3]


	#verify the enterd password
	if verify_password(password,password_hash):
		return 	True

	return False
