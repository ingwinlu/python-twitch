# -*- encoding: utf-8 -*-
"""
    twitch.api.v3.chat
    ~~~~~~~~~~~~~~~~~~

    This module implements the functionality described here
    https://github.com/justintv/Twitch-API/blob/master/v3_resources/chat.md

    .. autofunction:: by_channel(name)
    .. autofunction:: badges(name)
    .. autofunction:: emoticons()
"""

from twitch import keys
from twitch.queries import V3Query as Qry
from twitch.queries import query


@query
def by_channel(name):
    """Get links object to other chat endpoints
    
    :param name: Name of the channel
    :returns: JSON Object describing other chat endpoints
    """
    q = Qry('chat/{channel}')
    q.add_urlkw(keys.CHANNEL, name)
    return q


@query
def badges(name):
    """Get chat badges for channel

    :param name: Name of the channel
    :returns: JSON Object describing all channel badges
    """
    q = Qry('chat/{channel}/badges')
    q.add_urlkw(keys.CHANNEL, name)
    return q


@query
def emoticons():
    """Returns a list of all emoticon objects for Twitch.

    :returns: JSON Object describing all emoticon objects
    """
    q = Qry('chat/emoticons')
    return q
