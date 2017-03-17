from . import api
from .. import mongo

@api.route('/mongo')
def test():
    return ''