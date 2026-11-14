CC = gcc
CFLAGS = -Wall -Wextra -fPIC -O2 -Iinclude
LDFLAGS = -shared

SRC = src/hello.c
OBJ = hello.o
LIB = libhello.so

.PHONY: all clean

all: $(LIB)

$(LIB): $(OBJ)
	$(CC) $(LDFLAGS) -o $@ $^

$(OBJ): $(SRC) include/hello.h
	$(CC) $(CFLAGS) -c $(SRC) -o $@

clean:
	rm -f $(OBJ) $(LIB)
