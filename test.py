import asyncio


def just_func():
    pass


async def async_func():
    x = None
    return x


print(just_func)
print(async_func())
