from json import dumps

BOOKS = {
    '012': {
        'name': 'tom',
        'sex': 'woman',
        'address': 'anHui'
    },
    '013': {
        'name': 'Lily',
        'sex': 'woman',
        'address': 'shanghai'
    },
    '014': {
        'name': 'Jim',
        'sex': 'man',
        'address': 'beijing'
    }
}

print(dumps(BOOKS))

