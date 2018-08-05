from models.user import UserModel

# users = [
#     User(1, 'alex', 'password'),
#     User(2, 'keira', 'password')
# ]
#
# username_mapping = {user.username: user for user in users}
# userid_mapping = {user.id: user for user in users}

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
