import ctypes
import ctypes.util
from pathlib import Path

# -------------------------------------------------
# Load the shared library
# -------------------------------------------------
lib_path = Path(__file__).parent / "libhello.so"
if not lib_path.exists():
    raise FileNotFoundError(f"{lib_path} not found. Run `make` first.")

lib = ctypes.CDLL(str(lib_path))

# -------------------------------------------------
# Function signatures
# -------------------------------------------------
lib.hello_print.argtypes = [ctypes.c_char_p]
lib.hello_print.restype = None

lib.hello.argtypes = [ctypes.c_char_p]
lib.hello.restype = ctypes.c_void_p

# Load libc to get a proper free()
libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.free.argtypes = [ctypes.c_void_p]
libc.free.restype = None


# -------------------------------------------------
# Python wrappers
# -------------------------------------------------
def hello_print(name: str) -> None:
    lib.hello_print(name.encode("utf-8"))


def hello(name: str) -> str:
    ptr = lib.hello(name.encode("utf-8"))

    if not ptr:
        raise MemoryError("C function returned NULL")

    try:
        result = ctypes.string_at(ptr).decode("utf-8")
    finally:
        libc.free(ptr)

    return result


# -------------------------------------------------
# Demo
# -------------------------------------------------
if __name__ == "__main__":
    hello_print("Amirhossein")
    hello_print("RayID")

    print(hello("Amirhossein"))
    print(hello("World"))
