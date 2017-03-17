from app import creat_app, mongo
from config import RUN_LEVEL
from flask_script import Manager, Shell

app = creat_app(RUN_LEVEL)
manager = Manager(app)

def make_shell_context():
    return dict(app=app, mongo=mongo)
manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def test():
    """Run the unit test"""

if __name__ == '__main__':
    manager.run()