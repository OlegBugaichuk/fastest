from fastapi.routing import APIRoute
import inspect
from fastest.utils.generators import router_test_generator


def test_router_test_generator() -> None:
    route = APIRoute(path='/api/test/', endpoint=lambda: None)
    test_str: str = router_test_generator(route)
    assert route.path in test_str
