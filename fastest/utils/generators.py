from fastapi.routing import APIRoute
from jinja2 import Environment, PackageLoader, select_autoescape


def router_test_generator(route: APIRoute) -> str:
    """Generator tests for routers."""
    env = Environment(
        loader=PackageLoader('fastest', 'templates'),
        autoescape=select_autoescape(),
    )

    template = env.get_template('func.tmpl')
    return template.render(route=route)
