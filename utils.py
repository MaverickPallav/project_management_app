import random
import string

def generate_random_name(length=8):
    """Generate a random string of given length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def format_user_info(user):
    """Format user info as a string."""
    return f"{user.name} ({user.email})"
