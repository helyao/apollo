from . import auth

@auth.route('/test')
def test():
    return '<h1>hello auth</h1>'