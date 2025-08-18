from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class Postgres_Controller:
    def __init__(
            self,
            usuario = 'mi_usuario',
            passw = 'mi_contraseña',
            host = 'localhost',
            puerto = '5432',
            db = 'mi_basedatos',
            ):
        
        url = f"mysql+pymysql://{usuario}:{passw}@{host}:{puerto}/{db}"
        self.engine = create_engine(url)
        self.create_session()
    
    def create_session(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_model(self, Base):
        Base.metadata.create_all(self.engine)


    def get_all(self,model):
        return self.session.query(model).all()
    
    def create_record(self, model, info):
        new_record = model(**info)
        self.session.add(new_record)
        self.session.commit()
