class ApiRes:
    OK = (200, 'OK')
    CREATE = (201, 'created_successfully')
    BAD_REQUEST = (400, 'bad_request')
    BAD_USER_NAME = (401, 'username not empty')
    BAD_USER_PASSWORD = (402, 'password not empty')
    ERROR_USER_PASSWORD = (403, 'password error')
    NO_ACCESS = (410, 'forbidden')
    NOT_FOUND = (420, 'not_found')