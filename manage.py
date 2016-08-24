import os 
from app import create_app,db
from app.models import Student
from flask.ext.script import Shell
from flask.ext.script import  Manager,Server
from flask_migrate import Migrate,MigrateCommand


app = create_app(os.getenv('ACS_CONFIG') or 'default')
manager = Manager(app)
migrate =Migrate(app,db)

def make_shell_context():
    return dict(app=app,Student=Student,db=db)
manager.add_command('shell',Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)

if __name__=='__main__':
    manager.run()