from django.core.exceptions import ValidationError

from My_EShop.core.utils import megabytes_to_bytes


def validate_only_letters(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError(f'Only letters are allowed')


def validate_max_image_size(image):
    filesize = image.file.size
    megabyte_limit = 5.0
    if filesize > megabytes_to_bytes(megabyte_limit):
        raise ValidationError(f'Max file size is {megabyte_limit}MB')
