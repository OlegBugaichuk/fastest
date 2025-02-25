import argparse
import importlib
import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi.routing import APIRoute

from fastest.utils.generators import router_test_generator

sys.path.insert(0, str(Path.cwd()))


def get_tests_path() -> Path:
    """Check tests path exists, and return."""
    tests_path = Path.cwd() / 'tests'
    if not tests_path.exists():
        tests_path.mkdir()
    return tests_path


def get_app() -> FastAPI:
    """Get the FastAPI application."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'path', type=str, help='FastAPI application path. application.path:app',
    )
    module_path, app_path = parser.parse_args().path.rsplit(':', 1)
    module_obj = importlib.import_module(module_path)
    return getattr(module_obj, app_path)  # type: ignore[no-any-return]


def main() -> None:
    """Main function."""
    app = get_app()
    tests_path = get_tests_path()

    for router in app.routes:
        routers_tests_path = tests_path / 'routers.py'
        with routers_tests_path.open('a') as routers_tests_file:
            if isinstance(router, APIRoute):
                routers_tests_file.write(router_test_generator(router))


if __name__ == '__main__':
    main()
