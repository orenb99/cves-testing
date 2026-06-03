import pymysql


def connect_to_database():
    # Intentionally vulnerable to Hardcoded Credentials
    db_user = "admin"
    db_password = "SuperSecretPassword123!"

    connection = pymysql.connect(
        host='database.internal.local',
        user=db_user,
        password=db_password,
        database='production_db'
    )
    return connection