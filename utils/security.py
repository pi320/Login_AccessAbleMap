from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    return generate_password_hash(password, method = 'bcrypt')

def check_password(hash, password):
    """Check a hashed password against the input password."""
    return check_password_hash(hash, password)
