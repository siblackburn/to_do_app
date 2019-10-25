class Config(object):

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '12345'
    
    # sqlite
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

    # postgres
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='postgres',pw='mysecretpassword',url='localhost',db='postgres')

    # mysql
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://siblackburn:psw@localhost/task_list'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True