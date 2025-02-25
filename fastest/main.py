import argparse
import importlib
import sys
from pathlib import Path
from fastapi import FastAPI
from fastapi.routing import APIRoute

from http import HTTPStatus
from fastest.utils.generators import router_test_generator


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="FastAPI application path. application.path:app")
    args = parser.parse_args()

    cwd = Path.cwd()
    sys.path.insert(0, str(cwd))

    module_path, app_path = args.path.rsplit(":", 1)

    module_obj = importlib.import_module(module_path)

    app: FastAPI = getattr(module_obj, app_path)

    tests_path = cwd / "tests"

    if not tests_path.exists():
        tests_path.mkdir()

    for router in app.routes:
        routers_tests_path = tests_path / "routers.py"
        with routers_tests_path.open("a") as routers_tests_file:
            if isinstance(router, APIRoute):
                test = router_test_generator(router)
                routers_tests_file.write(test)


if __name__ == "__main__":
    main()
