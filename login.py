import hashlib
import secrets


def hash_password(password):
    """
    Convert a password into a SHA-256 hash.
    This keeps the stored password from being plain text.
    """
    return hashlib.sha256(password.encode()).hexdigest()


USER_DATABASE = {
    "student@example.com": {
        "password_hash": hash_password("password123")
    }
}


def login(email, password):
    """
    Log in a user with email and password.

    Returns:
        A dictionary with success = True and a token if login succeeds.
        A dictionary with success = False and an error message if login fails.
    """
    if not email or not password:
        return {
            "success": False,
            "error": "Email and password are required"
        }

    normalized_email = email.strip().lower()
    user = USER_DATABASE.get(normalized_email)

    if user is None:
        return {
            "success": False,
            "error": "Invalid email or password"
        }

    password_hash = hash_password(password)

    if password_hash != user["password_hash"]:
        return {
            "success": False,
            "error": "Invalid email or password"
        }

    token = secrets.token_hex(16)

    return {
        "success": True,
        "token": token
    }