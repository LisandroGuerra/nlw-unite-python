'''This module is responsible for handling the connection to the database.'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class _DBConnectionHandler:
    '''This class is responsible for handling the connection to the database. 
    It uses the SQLAlchemy library to connect to the database.'''
    def __init__(self) -> None:
        self.__db_engine = 'sqlite'
        self.__db_path = 'storage.db'
        self.__connection_string = f'{self.__db_engine}:///{self.__db_path}'
        self.__engine = None
        self.session = None


    def connect_to_db(self) -> None:
        '''This method is responsible for creating the connection to the database.'''
        self.__engine = create_engine(self.__connection_string)


    def get_engine(self):
        '''This method is responsible for returning the engine object.'''
        return self.__engine


    def __enter__(self):
        '''This method is responsible for creating the session object.'''
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        '''This method is responsible for closing the session object.'''
        self.session.close()
        self.__engine.dispose()

db_connection_handler = _DBConnectionHandler()
