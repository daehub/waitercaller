#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Daehub'

MOCK_USERS = [{'email':'test@example.com','salt':"""b'uQuP0/D9kL/oY/N46zlToYd/ayo='""",'hashed':'24b183ec5c404b60d002ee6244c6b55bbac65267662a2ef6100293ab99997f829a3c6b90cd58a1abee87acbd8702edcfbe885b4a335689bf43ee1333cd9e0df5'}]


class MockDBHelper(object):
    def get_user(self,email):
        user = [x for x in MOCK_USERS if x.get('email')==email]
        if user:
            return user[0]
        return None

    def add_user(self,email,salt,hashed):
        MOCK_USERS.append({'email':email,'salt':salt,'hashed':hashed})
