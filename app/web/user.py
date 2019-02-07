from app.web.blueprint import web


@web.route('/')
def user():
    return 'User page!'