from sys import argv
from config import *


def main(host, port):
    app.run(host=host, port=port)


if __name__ == "__main__":
    # main(argv[0:])
    main("127.0.0.1", 8080)
