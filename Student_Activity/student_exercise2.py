print()
def print_pattern(n):
    if n == 0:
        return
    print_pattern(n - 1)
    print("*" * n)
n=4
print_pattern(n)
print()