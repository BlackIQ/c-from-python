#ifndef HELLO_H
#define HELLO_H

#ifdef __cplusplus
extern "C"
{
#endif
    /**
     * Returns a greeting string.
     * The returned pointer must be freed by the caller using free().
     */
    char *hello(const char *name);

    /**
     * Prints a greeting directly to stdout.
     */
    void hello_print(const char *name);

#ifdef __cplusplus
}
#endif

#endif // HELLO_H
