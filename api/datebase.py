import mysql.connector

class DatabaseConnection:
    _connection = None
    _config = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
                host = cls._config['DATABASE_HOST'],
                user = cls._config['DATABASE_USERNAME'],
                port = cls._config['DATABASE_PORT'],
                password = cls._config['DATABASE_PASSWORD']
            )
        
        return cls._connection

    @classmethod
    def set_config(cls, config):
        cls._config = config
    
    @classmethod
    def execute_query(cls, query, database_name=None, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        cls._connection.commit()
        
        return cursor
    
    @classmethod
    def fetch_all(cls, query, database_name=None, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    
    @classmethod
    def fetch_one(cls, query, database_name=None, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        
        return cursor.fetchone()
    
    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None