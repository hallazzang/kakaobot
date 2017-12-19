# Represents Message object
# Ref: https://github.com/plusfriend/auto_reply#62-message
class Message:
    def __init__(self, text, *, photo=None, button=None):
        self.text = text
        if photo and not isinstance(photo, Photo):
            raise TypeError('Only Photo instance can be attached to a message')
        self.photo = photo
        if button and not isinstance(button, MessageButton):
            raise TypeError('Only MessageButton instance can be attached to a '
                            'message')
        self.button = button

# Represents Photo object
# Ref: https://github.com/plusfriend/auto_reply#63-photo
class Photo:
    def __init__(self, url, width, height):
        self.url = url
        self.width = width
        self.height = height

# Represents MessageButton object
# Ref: https://github.com/plusfriend/auto_reply#621-messagebutton
class MessageButton:
    def __init__(self, label, url):
        self.label = label
        self.url = url

