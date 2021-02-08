import base64

from django import template

register = template.Library()


@register.filter
def image_as_base64(image):
    if not image:
        return

    try:
        image_format = image.content_type.split('/')[1].lower()
        image_b64 = base64.b64encode(image.read())
        encoded_string = str(image_b64, 'utf8')
        return 'data:image/%s;base64,%s' % (image_format, encoded_string)
    except Exception as error:
        pass
