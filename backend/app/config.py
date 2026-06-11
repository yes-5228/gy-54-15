import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///grades.db",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")
    SEED_DEMO_DATA = os.getenv("SEED_DEMO_DATA", "true").lower() in ("true", "1", "yes")
