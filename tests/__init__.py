import logging
import os
import twitch

logging.basicConfig(level=logging.DEBUG)

ci = False
if os.environ.get('CI') == 'true':
    ci = True

if(ci):
    # raise retries on CI since travis connections are unstable
    twitch.MAX_RETRIES = 10
