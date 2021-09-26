from application_services.BaseApplicationResource import BaseApplicationResource
import database_services.RDBService as d_service


class UserResource(BaseApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_full_resource(cls, name_prefix):
        res = d_service.get_full_resource("user_resource", "user")
        return res