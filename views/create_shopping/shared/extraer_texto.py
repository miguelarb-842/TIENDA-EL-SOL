import io
import contextlib
import data

def capturar_print(
    func,
    *args,
    **kwargs
    ) -> str:

    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        func(*args, **kwargs)
    return buffer.getvalue()