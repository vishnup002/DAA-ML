#non-recursive

# def fibonacci_iterative(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         fib = [0, 1]
#         for i in range(2, n+1):
#             fib.append(fib[i-1] + fib[i-2])
#         return fib[n]
#
# print(fibonacci_iterative(10))

#recursive
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(10))