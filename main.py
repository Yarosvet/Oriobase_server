from sys import argv
from config import *


def main(host, port):
    db_session.global_init("database.sql")
    app.run(host=host, port=port)


if __name__ == "__main__":
    # main(argv[-2:])
    main("127.0.0.1", 8080)
