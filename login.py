USERS = {
    "admin": "admin123",
    "farmer": "farmer123"
}


def authenticate(
    username,
    password
):

    return (
        USERS.get(username)
        == password
    )