import os
from dotenv import load_dotenv
load_dotenv()


DB_USER = os.getenv('DB_USER', 'appuser')
DB_PASS = os.getenv('DB_PASS', 'apppassword')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'three_tier_app')
SECRET_KEY = os.getenv('SECRET_KEY', 'secret')
JWT_EXP_SECONDS = 3600


SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
