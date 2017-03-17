class Config(object):
    @staticmethod
    def init_app(app):
        pass

class TestingConfig(Config):
    DEBUG = True
    # Init settings
    INIT_DB_CLEAN_CONF = True
    INIT_DB_CLEAN_DATA = True
    INIT_EQUIP_LIST = ["669B0323", "9B98D70E"]
    INIT_USER_LIST = [
        ["test1", "111111"],
        ["test2", "222222"],
        ["test3", "333333"],
        ["test4", "444444"],
        ["test5", "555555"]
    ]
    # MongoDB settings
    MONGO_HOST = '127.0.0.1'
    MONGO_PORT = 27017

class DevelopmentConfig(Config):
    pass

class ProductionConfig(Config):
    pass

config = {
    'testing': TestingConfig,           # Windows PC
    'development': DevelopmentConfig,   # Linux PC
    'product': ProductionConfig         # Production Server
}

RUN_LEVEL = 'testing'