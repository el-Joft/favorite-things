from functools import wraps
from favorite_things.utils.error_handler import errors
from favorite_things.utils.database import get_existing_model
from favorite_things.apps.favorite.models import Favorite


class FavoriteValidation:
    """
    This class contains methods to help with validating Favorite.
    """

    def __call__(self, func):  # noqa
        @wraps(func)
        def wrapper(*args, **kwargs):
            valid_type = ['int', 'str', 'datetime', 'list']
            invalid_errors = []
            for field, field_value in kwargs.items():
                if field == 'title':
                    if field_value.strip() == '':
                        invalid_errors.append('Title cannot be empty')
                    get_existing_model(Favorite, 'title', field_value)
                if field == 'category':
                    if field_value.strip() == '':
                        invalid_errors.append('category cannot be empty')
                if field == 'ranking':
                    if field_value < 1:
                        invalid_errors.append('Ranking cannot be zero or less')
                if field == 'metadata':
                    for index in field_value:
                        data_type = type(index['content'])
                        if data_type.__name__ not in valid_type:
                            invalid_errors.append(
                                'data can only Number, Text, Date and Enum'
                            )

            if len(invalid_errors) >= 1:
                errors.custom_message(invalid_errors)
            return func(*args, **kwargs)

        return wrapper


favorite_validation = FavoriteValidation()
