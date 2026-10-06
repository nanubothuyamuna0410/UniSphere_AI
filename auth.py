USERS = {
    "student": {"password": "student123", "role": "student"},
    "admin": {"password": "admin123", "role": "admin"}
}

def login(username, password):
    if username in USERS and USERS[username]["password"] == password:
        return USERS[username]["role"]
    return None
