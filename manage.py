from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from blog import create_app, db

manager = Manager(create_app, db)
# 数据库迁移
Migrate(create_app, db)
manager.add_command('db', MigrateCommand)

app = create_app('development')


@app.route('/index')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()
