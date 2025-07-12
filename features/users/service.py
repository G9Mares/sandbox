from controllers.postgres_controller import Postgres_Controller
from .model import Users

controller = Postgres_Controller()


def service_get_users():
    usarios = controller.get_all(Users)
    return usarios