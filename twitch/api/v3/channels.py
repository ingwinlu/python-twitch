# -*- encoding: utf-8 -*-
"""
    twitch.api.v3.channels
    ~~~~~~~~~~~~~~~~~~~~~~

    This module implements the functionality described here 
    https://github.com/justintv/Twitch-API/blob/master/v3_resources/channels.md

    .. autofunction:: by_name(name)
    .. autofunction:: teams(name)
"""

from twitch import keys
from twitch.queries import V3Query as Qry
from twitch.queries import query

from .videos import by_channel


@query
def by_name(name):
    """Get channel object by name.

    :param name: Name of the channel
    :returns: Channel Object as JSON
    """
    q = Qry('channels/{channel}')
    q.add_urlkw(keys.CHANNEL, name)
    return q


@query
def channel():
    raise NotImplementedError


def get_videos(name, **kwargs):
    """Synonym for videos.by_channel"""
    return by_channel(name, **kwargs)


# TODO needs authentification
@query
def editors(name):
    raise NotImplementedError


# TODO needs authentification and put requests
@query
def update(name, status=None, game=None, delay=0):
    raise NotImplementedError


# TODO needs auth
@query
def delete(name):
    raise NotImplementedError


# TODO needs auth, needs POST request
@query
def commercial(name, length=30):
    raise NotImplementedError


@query
def teams(name):
    """Returns team objects associated with the channel

    :param name: Name of the channel
    :returns: Channel Object as JSON
    """
    q = Qry('channels/{channel}/teams')
    q.add_urlkw('channel', name)
    return q
