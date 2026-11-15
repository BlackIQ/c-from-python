# Calling C from Python with ctypes

Minimal example of writing a small C library and calling it from Python using `ctypes`. There is another repository for [Python C API](https://github.com/BlackIQ/python-c-api) that you can check them out.

Just a personal learning note.

## How Does It Work?

Consider we define our functions in C. Out Python project can call those C functions! So, **MAGIC**!

## Requirements

- Python
- GCC
- C compiler supported by your Python

## Setup

Clone the repo as usual and cd into it. After that follow steps below.

### Build

Here you should build to get lib files.

```bash
make
```

## Run

Then it's time to run it to see how is it working.

```bash
python test.py
```

## Notes

- The C code is compiled as a shared library (`.so`)
- Memory allocated in C is freed from Python
- Uses pure `ctypes` (no Cython or Python C API)
