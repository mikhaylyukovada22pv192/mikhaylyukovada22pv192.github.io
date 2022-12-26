import json

from aiohttp import web

from database.database_api import get_all_capability, create_capability, add_capability
from database.models import Capability


def operation_to_dict(operation: tuple, number: int):
    result: dict = {
        'id': number,
        'img_name': operation[1],
        'title': operation[2],
        'description': operation[3],
        'more_info': operation[4],
        'info_image': operation[5]}
    return result


async def get_capabilities(request: web.Request) -> web.Response:
    results = get_all_capability(request)

    response = []
    for number, r in enumerate(results):
        response.append(operation_to_dict(r, number + 1))
    return web.json_response(text=json.dumps(response))


async def post_capability(request: web.Request) -> web.Response:
    body = await request.json()
    capability: Capability = create_capability(
        body["img_name"],
        body["title"],
        body["description"],
        body["more_info"],
        body["info_image"])
    add_capability(capability)

    response: dict = dict()
    response['id'] = capability.id
    response['img_name'] = capability.img_name
    response['title'] = capability.title
    response['description'] = capability.description
    response['more_info'] = capability.more_info
    response['info_image'] = capability.info_image

    return web.json_response(text=json.dumps(response))
