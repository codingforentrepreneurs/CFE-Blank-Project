from cfehome.env import config

POSTGRES_USER = config("POSTGRES_USER", default=None)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", default=None)
POSTGRES_DB = config("POSTGRES_DB", default=None)
POSTGRES_HOST = config("POSTGRES_HOST", default=None)
POSTGRES_PORT = config("POSTGRES_PORT", default=None)
POSTGRES_DB_IS_AVAIL = all(
    [POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_HOST, POSTGRES_PORT]
)
POSTGRES_DB_REQUIRE_SSL = config("POSTGRES_DB_REQUIRE_SSL", cast=bool, default=False)

if POSTGRES_DB_IS_AVAIL:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": POSTGRES_DB,
            "USER": POSTGRES_USER,
            "PASSWORD": POSTGRES_PASSWORD,
            "HOST": POSTGRES_HOST,
            "PORT": POSTGRES_PORT,
        }
    }
    if POSTGRES_DB_REQUIRE_SSL:
        DATABASES["default"]["OPTIONS"] = {"sslmode": "require"}
