import ZODB

__root = None

def get_root():
    global __root
    if not __root:
        db = ZODB.DB('controlador/data/data/db.fs')
        connection = db.open()
        __root  = connection.root
    return __root

