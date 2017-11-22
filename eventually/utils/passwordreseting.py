"""
Password reseting
=========

The module that provides functions for sending reset password letter to user and reseting password.
"""

from eventually.settings import FRONT_HOST
from utils.jwttoken import create_token
from utils.send_mail import send_email

TTL_SEND_PASSWORD_TOKEN = 60 * 60

def send_password_update_letter(user):
    """
    Function that provides sending update password letter to user.

    :param user: user that we want send letter to.
    :type user: CustoUser obj

    :return: True if letter was send else None.
    """

    arg = {'user_id': user.id}
    token = create_token(data=arg, expiration_time=TTL_SEND_PASSWORD_TOKEN)
    ctx = {'first_name': user.first_name,
           'token': token,
           'domain': FRONT_HOST}
    subject = 'Pasword reset'
    message = 'You tried to change your password.'
    recipient_list = [user.email]
    template = 'change_password_link.html'
    if send_email(subject, message, recipient_list, template, ctx):
        return True


def send_successful_update_letter(user):
    """
    Function that provides sending successful update letter.

    :param user: user that we want send letter to.
    :type user: CustoUser obj


    :return: True if letter was send else None.
    """

    ctx = {'first_name': user.first_name}
    subject = 'Pasword reset'
    message = 'Successful pasword reset.'
    recipient_list = [user.email]
    template = 'update_password.html'
    if send_email(subject, message, recipient_list, template, ctx):
        return True
