Quickstart
==========

.. warning::

        This documentation is currently a work in progress and is still rough
        around the edges. Not finding what you are looking for? Please open an
        issue describing your troubles on `python-twitch's github page`_!


Installation
------------

python-twitch can be installed via::

    pip install python-twitch

For a more unstable version you can directly install from the github
repository::

    pip install -e git+https://github.com/ingwinlu/python-twitch


Dependencies
------------

python-twitch supports Python 2.7 and Python 3.3+. It's only dependency is six_
which should be automatically be installed when you install python-twitch.


Usage
-----

No additional setup is required, choose which API's you want to use and import
them. python-twitch also does some logging. For troubleshooting add a handler to
`twitch.logging.log`.


API
+++

Choose which ever API's you want to use and import them into your project::

    from twitch.api import v3
    v3.streams.all(limit=1)


Responses
+++++++++

All queries executed over python-twitch result in json responses. You can find
more information on them on the official twitch api documentation. Inofficial
api's don't have any documentation and might get changed anytime, so don't build
reliable systems around them and expect the results to change without warning.


Logging
+++++++

To have access to python-twitchs logging output add a handler to
twitch.logging.log::

    import logging
    from twitch.logging import log

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
                    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log.addHandler(console_handler)


.. links:

.. _six: http://pythonhosted.org/six/
.. _`python-twitch's github page`: https://github.com/ingwinlu/python-twitch
