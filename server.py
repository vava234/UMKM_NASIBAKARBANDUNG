import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parent


class WebsiteHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)


def main():
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "5500"))
    server = ThreadingHTTPServer((host, port), WebsiteHandler)
    print(f"Website berjalan di http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
