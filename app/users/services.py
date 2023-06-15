from app.models import User

def fetch_user(user_id):
    user = User.query.get(user_id)
    if user:
        return True, {'username': user.username, 'email': user.email}
    else:
        return False, {'error': 'User not found'}

def create_user(data):
    username = data.get('username')
    email = data.get('email')

    if not username or not email:
        return False, {'error': 'Invalid data'}

    user = User(username=username, email=email)
    # user.set_password(password)

    # db.session.add(user)
    # db.session.commit()

    return True, {'username': user.username, 'email': user.email}
