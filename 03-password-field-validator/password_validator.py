ERROR_MESSAGES = {
    'LENGTH': 'Password must be at least 8 characters'
}


def password_validator(password):
    if len(password) < 8:
        return (False, ERROR_MESSAGES['LENGTH'])

    return (True, None)
