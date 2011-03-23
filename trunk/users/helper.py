# -*- coding: utf-8 -*-

import hashlib
from django.core.mail import send_mail
from django.template import Context, loader

def get_sig(username):
    base_str = ['%si' %i for i in username]
    sig = username + hashlib.new('md5', "".join(base_str)).hexdigest()
    return sig

def send_active_mail(user):
    subject = "<爱某人>网站账号激活"
    t = loader.get_template('users/active_email.html')
    sig = get_sig(user.username)
    hex_sig = hashlib.new('md5', sig).hexgiest()
    active_url = "%s/users/active_account/?username=%s&sig=%s" \
            %(settings.SITE_URL, user.username, hex_sig)
    c = Context({
            'active_url': active_url,
            'username': user.username,
        })
    send_mail(subject, t.render(c), '"爱某人"<noreply@imouren.com>', \
            [user.username,])

if __name__ == "__main__":
    sig = get_sig('mouren')
    print sig
    send_mail('hello', "hello, mouren", '"爱某人"<noreply@imouren.com>', ['mouren11@163.com'])

