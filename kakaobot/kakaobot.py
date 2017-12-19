import inspect

from aiohttp import web

from .types import Message, Photo, MessageButton

class KakaoBot:
    def __init__(self):
        self.app = web.Application()

        # Empty handlers
        self.handlers = {
            name: None for name in (
                'keyboard',
                'message',
                'friend_add',
                'friend_delete',
                'leave_room',
            )
        }

    def run(self, **kwargs):
        self.app.router.add_get('/keyboard', self._on_keyboard)
        self.app.router.add_post('/message', self._on_message)
        web.run_app(self.app, **kwargs)

    async def _on_keyboard(self, request):
        if self.handlers['keyboard']:
            resp = await self._get_result(self.handlers['keyboard'])
            if resp is None:  # Use default keyboard
                return web.json_response({'type': 'text'})
            elif isinstance(resp, (tuple, list)):  # Use button keyboard
                return web.json_response({'type': 'buttons', 'buttons': resp})
            else:
                raise TypeError('Invalid response')
        else:
            # Default keyboard
            return web.json_response({'type': 'text'})

    async def _on_message(self, request):
        if self.handlers['message']:
            req = await request.json()  # Could fail, but not in production
            resp = await self._get_result(self.handlers['message'],
                req['user_key'], req['type'], req['content'])
            if isinstance(resp, str):  # Simple text response
                return web.json_response({'text': resp})
            elif isinstance(resp, Message):  # Complex message response
                r = {'text': resp.text}
                if resp.photo:
                    r['photo'] = {
                        'url': resp.photo.url,
                        'width': resp.photo.width,
                        'height': resp.photo.height,
                    }
                if resp.button:
                    r['message_button'] = {
                        'label': resp.button.label,
                        'url': resp.button.url,
                    }
                return web.json_response(r)
            else:
                raise TypeError('Invalid response')
        else:
            # Default response
            return web.json_response({'text': 'Default response'})

    def __getattr__(self, name):
        if name.startswith('on_'):
            if name[3:] in self.handlers:
                def _register_handler(handler):
                    self.handlers[name[3:]] = handler
                return _register_handler
            else:
                raise AttributeError('Unknown handler: %s' % name[3:])
        else:
            return super().__getattribute__(name)

    async def _get_result(self, handler, *args, **kwargs):
        if inspect.iscoroutinefunction(handler):
            return await handler(*args, **kwargs)
        else:
            return handler(*args, **kwargs)

