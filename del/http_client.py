import aiohttp
import async_timeout


__all__ = ('http',)


async def http(url: str, json: dict=None, headers: dict=None, timeout=15, method='POST'):
    """Async HTTP client."""
    if headers is None:
        headers = {}

    with async_timeout.timeout(timeout):
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.request(method, url, json=json) as response:
                data = await response.json()
                return response, data
