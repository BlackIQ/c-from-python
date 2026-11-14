#include "hello.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *hello(const char *name)
{
    if (name == NULL)
    {
        name = "World";
    }

    size_t len = strlen("Hello, ") + strlen(name) + 2;
    char *result = (char *)malloc(len);

    if (result == NULL)
    {
        return NULL;
    }

    snprintf(result, len, "Hello, %s!", name);

    return result;
}

void hello_print(const char *name)
{
    if (name == NULL)
    {
        name = "World";
    }

    printf("Hello, %s!\n", name);
}