import os

class Config:
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	UPLOADED_PHOTOS_DEST ='app/static/photos'
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/database_name'

	@staticmethod
	def init_app(app):
		pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}