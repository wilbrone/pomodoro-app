import os

class Config:
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	UPLOADED_PHOTOS_DEST ='app/static/photos'
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://aphya5:NewPasword@localhost/pomodoro'

	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

	@staticmethod
	def init_app(app):
		pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://aphya5:NewPasword@localhost/pomodoro'
	DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
