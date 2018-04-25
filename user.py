#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Daehub'


class User (object):
    def __init__(self,email):
        self.email = email

    def get_id(self):
        return self.email

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True