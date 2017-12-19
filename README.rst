========
kakaobot
========

Super simple framework for Kakaotalk auto-reply bot based on aiohttp

Installation
------------

.. code::

    $ pip3 install --upgrade python-kakaobot

Example
-------

From ``examples/simple_echo.py``:

.. code:: python

    from kakaobot import KakaoBot

    bot = KakaoBot()

    @bot.on_message
    async def handle_message(message, **args):
        if args['type'] == 'text':
            return 'Echoing: %s' % message
        else:
            return 'Cannot understand'

    if __name__ == '__main__':
        bot.run(host='0.0.0.0', port=8080)

Nice, isn't it?

Why not Flask or Django?
------------------------

Because setting up full Flask/Django development environment is a bit of pain,
especially for this kind of tiny application with no front-end view.
It is well-known using default development server for Flask/Django is not the way
you run your web application. But in aiohttp, it is. That's why I chose aiohttp.

