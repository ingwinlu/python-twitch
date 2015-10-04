# -*- encoding: utf-8 -*-
"""
    twitch.api.v3.blocks
    ~~~~~~~~~~~~~~~~~~~~

    This module implements the functionality described here
    https://github.com/justintv/Twitch-API/blob/master/v3_resources/blocks.md
"""

from twitch.queries import query


# Needs Authentification
@query
def by_name(user):
    raise NotImplementedError


# Needs Authentification, needs PUT
@query
def add_block(user, target):
    raise NotImplementedError


# Needs Authentification, needs DELETE
@query
def del_block(user, target):
    raise NotImplementedError
