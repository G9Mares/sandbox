from controllers.postgres_controller import Postgres_Controller
from .model import Users

controller = Postgres_Controller()

class User_service:
    
    def service_get_users(self):
        usarios = controller.get_all(Users)
        return usarios