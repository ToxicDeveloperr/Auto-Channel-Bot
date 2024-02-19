import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', True)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', '27710337'))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', '354e1dd8e1e3041ee2145196da8d6aac')
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '6586197313:AAHUPxFsJTV7FkoxnItFyGxQFeXoPc4ts0g')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'mongodb+srv://tejaschavan1110:AE8y3iL6UVLpOy3K@cluster0.hlutxwm.mongodb.net/?retryWrites=true&w=majority')
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', 'movies_market_backup')
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 0
    API_HASH = ""
    BOT_TOKEN = ""
    DATABASE_URL = ""
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = ""
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
