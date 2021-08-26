from sys import argv
import api.v1
from config import *


def main(host, port):
    db_session.global_init("database.sqlite")
    app.add_url_rule("/api/v1/get_object/<int:object_id>", api.v1.get_object)
    app.run(host=host, port=port)


if __name__ == "__main__":
    # main(argv[-2:])
    main("127.0.0.1", 8080)
