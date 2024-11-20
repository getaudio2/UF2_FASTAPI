def user_schema(user) -> dict:
    return {"name": user[0],
            "surname": user[1],
            "age": user[2],
            "email": user[3]
            }

def users_schema(users) -> list[dict]:
    return [user_schema(user) for user in users]