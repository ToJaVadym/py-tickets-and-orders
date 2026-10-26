from db.models import User


def create_user(username: str, password: str, email: str = None, first_name: str = None, last_name: str = None) -> User:
    names_dict = {}
    if first_name:
        names_dict['first_name'] = first_name
    if last_name:
        names_dict['last_name'] = last_name
    user = User.objects.create_user(username=username, password=password, email=email, **names_dict)
    return user

def get_user(user_id: int) -> User:
    return User.objects.get(pk=user_id)

def update_user(user_id:int, password: str = None, username: str = None, email: str = None, first_name: str = None, last_name: str = None) -> User:
    user = User.objects.get(pk=user_id)
    if username:
        user.username = username
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    if email:
        user.email = email
    if password:
        user.set_password(raw_password=password)
    user.save()
    return user