from sys import argv
import api.v1
from config import *


def main(host, port):
    db_session.global_init("database.sqlite")
    app.add_url_rule(rule="/api/v1/get_object", view_func=api.v1.get_object)
    app.add_url_rule(rule="/api/v1/get_objectgroup", view_func=api.v1.get_object_group)
    app.add_url_rule(rule="/api/v1/new_object", view_func=api.v1.new_object)
    app.add_url_rule(rule="/api/v1/new_objectgroup", view_func=api.v1.new_object_group)
    app.add_url_rule(rule="/api/v1/set_object", view_func=api.v1.set_object)
    app.add_url_rule(rule="/api/v1/set_objectgroup", view_func=api.v1.set_object_group)
    app.run(host=host, port=port)


if __name__ == "__main__":
    # main(argv[-2:])
    main("127.0.0.1", 8080)
