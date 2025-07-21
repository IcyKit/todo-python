from fastapi import Request


async def log_request(request: Request, call_next):
    print('Это Middleware который я реализую потом')
    response = await call_next(request)
    return response
