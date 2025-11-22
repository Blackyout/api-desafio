from .base import *
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

# Database: Lee de DATABASE_URL
DATABASES = {
    "default": dj_database_url.config(default="sqlite:///db.sqlite3")
}

# CORS Config
CORS_ALLOWED_ORIGINS = os.environ.get("CORS_ALLOWED_ORIGINS", "http://localhost:4200").split(",")