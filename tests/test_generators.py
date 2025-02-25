from fastapi.routing import APIRoute

from fastest.utils.generators import router_test_generator


def test_router_test_generator() -> None:
    """Check test router generator."""
    route = APIRoute(path='/api/test/', endpoint=lambda: None)
    test_str: str = router_test_generator(route)
    assert route.path in test_str
