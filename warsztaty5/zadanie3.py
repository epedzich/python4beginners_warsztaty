def fibonnacci(elements_limit=None):
    if elements_limit == 0:
        return
    if elements_limit == 1:
        yield 0
        return

    a = 0
    b = 1
    yield a
    yield b

    i = 2
    while elements_limit is None or i < elements_limit:
        i += 1

        a, b = b, a + b
        yield b
