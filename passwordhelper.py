#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Daehub'


import base64
import hashlib
import os


class PasswordHelper(object):
    def get_hash(self, plain):
        hash_SHA = hashlib.sha512()
        hash_SHA.update(plain.encode('utf-8'))
        return hash_SHA.hexdigest()

    def get_salt(self):
        return base64.b64encode(os.urandom(20))

    def validate_password(self, plain, salt, expected):
        hashed = self.get_hash(plain+salt)
        result = (hashed == expected)
        return result


if __name__ == '__main__':
    plain = '123456'
    password = PasswordHelper()
    salt = password.get_salt()
    salt = """b'uQuP0/D9kL/oY/N46zlToYd/ayo='"""

    hashed = password.get_hash(plain+salt)

    print(hashed)
    print(salt)
    print(password.validate_password(plain, salt,'ab66d234b89fa4ca47939b28f4869e77a8780b2c4d976a9e511b916e21519ca91c90ba77e3f40ec12bc1dea81604c0544a53423bc393d104e139357f69e88029'))