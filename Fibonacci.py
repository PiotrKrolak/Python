# rekurencja & fibonacci

fibonacci_cache = {}

def fibonacci_1(n):
    if n ==1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_1(n-1) + fibonacci_1(n-2)


def fibonacci_c(n):
    # If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth term
    if n == 1:
        Value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_c(n-1) + fibonacci_c(n-2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value


###########################################
for n in range(1, 51):
    print(fibonacci_c(n))
