CC = gcc
CFLAGS = -Wall -Wextra -fPIC -O2
LDFLAGS = -shared

LIB = libhello.so
OBJS = hello.o

all: $(LIB)

$(LIB): $(OBJS)
	$(CC) $(LDFLAGS) -o $@ $^

%.o: %.c hello.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(LIB)

.PHONY: all clean