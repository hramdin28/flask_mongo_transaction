import os

from app import create_app

PROFILE = 'PROFILE'
app = create_app(os.getenv(PROFILE, 'dev'))

if __name__ == '__main__':
    app.run()
