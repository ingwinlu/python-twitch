# -*- encoding: utf-8 -*-
"""
    twitch.api.v3.follows
    ~~~~~~~~~~~~~~~~~~~~~

    This module implements the functionality described here
    https://github.com/justintv/Twitch-API/blob/master/v3_resources/follows.md

    .. autofunction:: by_channel(name, limit=25, offset=0, direction=Direction.DESC)
    .. autofunction:: by_user(name, limit=25, offset=0, direction=Direction.DESC, sort_by=SortBy.CREATED_AT)
    .. autofunction:: status(user, target)
"""

from twitch import keys
from twitch.api.parameters import Direction, SortBy
from twitch.queries import V3Query as Qry
from twitch.queries import query


@query
def by_channel(name, limit=25, offset=0, direction=Direction.DESC):
    """Get channel's list of following users

    :param name: Name of the channel
    :param limit: Maximum number of objects in array. Default is 25. Maximum is 100.
    :param offset: Object offset for pagination. Default is 0.
    :param direction: Creation date sorting direction. Default is desc. Valid values are asc and desc.
    :returns: JSON List of Follow objects
    """
    q = Qry('channels/{channel}/follows')
    q.add_urlkw(keys.CHANNEL, name)
    q.add_param(keys.LIMIT, limit, 25)
    q.add_param(keys.OFFSET, offset, 0)
    q.add_param(keys.DIRECTION, direction, Direction.DESC)
    return q


@query
def by_user(name, limit=25, offset=0, direction=Direction.DESC,
            sort_by=SortBy.CREATED_AT):
    q = Qry('users/{user}/follows/channels')
    q.add_urlkw(keys.USER, name)
    q.add_param(keys.LIMIT, limit, 25)
    q.add_param(keys.OFFSET, offset, 0)
    q.add_param(keys.DIRECTION, direction, Direction.DESC)
    q.add_param(keys.SORT_BY, sort_by, SortBy.CREATED_AT)
    return q


@query
def status(user, target):
    q = Qry('users/{user}/follows/channels/{target}')
    q.add_urlkw(keys.USER, user)
    q.add_urlkw(keys.TARGET, target)
    return q


# Needs Auth, needs PUT
@query
def follow(user, target):
    raise NotImplementedError


# Needs Auth, needs DELETE
@query
def unfollow(user, target):
    raise NotImplementedError


# Needs Auth
@query
def streams():
    raise NotImplementedError
