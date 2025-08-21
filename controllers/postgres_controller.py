from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from functools import wraps
from sqlalchemy.orm.session import Session

def play_session(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        with self.session_maker() as session:
            return func(self, session, *args, **kwargs)
    return wrapper

def transactional(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        with self.session_maker() as session:
            try:
                result = func(self, session, *args, **kwargs)
                session.commit()
                return result
            except:
                session.rollback()
                return False
    return wrapper


class Postgres_Controller:
    def __init__(
            self,
            usuario = 'mi_usuario',
            passw = 'mi_contraseña',
            host = 'localhost',
            puerto = '5432',
            db = 'mi_basedatos',
            ):
        
        url = f"postgresql+psycopg2://{usuario}:{passw}@{host}:{puerto}/{db}"
        self.engine = create_engine(url)    
        self.session_maker = sessionmaker(bind=self.engine)


    def create_model(self, Base):
        Base.metadata.create_all(self.engine)


    @play_session
    def get_all(self,session:Session ,model):
        return session.query(model).all()
    
    @transactional
    def create_record(self, session:Session, model, info):
        new_record = model(**info)
        session.add(new_record)
        return new_record