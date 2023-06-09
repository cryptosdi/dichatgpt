class ApiRes:
    OK = (200, 'OK')
    CREATE = (201, 'created_successfully')
    CONTENT_EMPTY = (300, 'content empty')
    BAD_REQUEST = (400, 'bad_request')
    BAD_USER_NAME = (401, 'username not empty')
    BAD_USER_PASSWORD = (402, 'password not empty')
    ERROR_USER_PASSWORD = (403, 'password error')
    NO_ACCESS = (410, 'forbidden')
    EXPIRED_TOKEN = (411, 'EXPIRED TOKEN')
    NO_TOKEN = (412, 'no token')
    LIMIT_API = (413, 'limit api')
    NOT_FOUND = (420, 'not_found')
    SERVICE_ERROR = (500, 'service error')