from sqlalchemy import create_engine
from models import Base
from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

print("Creating database tables...")
Base.metadata.create_all(engine)
print("Tables created successfully.")

