import argparse
import socket
import sys
from urllib import request


def get_arguments():
    """
    Get the arguments using argparser and return values.
    """
    parser = argparse.ArgumentParser(description="Check if the server is running.")
    parser.add_argument("--host", default="localhost", help="The host to check.")
    parser.add_argument("--port", default=8010, help="The port to check.", type=int)
    parser.add_argument("--timeout", default=5, help="The timeout to check.", type=int)
    parser.add_argument("--path", default="utils/health", help="The timeout to check.")
    return parser.parse_args()


def healthcheck(host, port, path, timeout=5):
    """
    Check if the server is running.
    Return True if the status code is 200, otherwise False.
    """
    try:
        response = request.urlopen(f"http://{host}:{port}/{path}", timeout=timeout)
        return response.code == 200
    except socket.error:
        return False


if __name__ == "__main__":
    """
    Run this script to check if the server is running.
    with the following command:
    python3 healthcheck.py --host <host> --port <port> --timeout <timeout>
    """
    args = get_arguments()
    host, port, path, timeout = args.host, args.port, args.path, args.timeout
    status = healthcheck(host=host, port=port, path=path, timeout=timeout)

    sys.exit(0) if status else sys.exit(1)
