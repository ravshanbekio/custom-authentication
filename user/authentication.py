from user.models import Account

class AccountAuthentication(object):
    def authenticate(self, username=None, email=None, password=None):
        try:
            user = Account.objects.get(username=username)
            if user.check_password(password) and user.email==email:
                return user
            return None
        except Account.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Account.objects.get(id=user_id)
        except Account.DoesNotExist:
            return None