import os
from app import create_app
from app.db_con import create_tables


app = create_app('development')


if __name__ == '__main__':
    create_tables()
    app.run(debug=True,)