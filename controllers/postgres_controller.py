from sqlalchemy.orm import Session



class Postgres_Controller:
    def __init__(self, session:Session):
        self.session = session

    def get_all(self,model):
        return self.session.query(model).all()