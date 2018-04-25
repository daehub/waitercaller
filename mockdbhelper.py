#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Daehub'

MOCK_USERS = {'test@example.com': '123456'}


class MockDBHelper(object):
    def get_user(self,email):
        if email in MOCK_USERS:
            return MOCK_USERS[email]
        return None
