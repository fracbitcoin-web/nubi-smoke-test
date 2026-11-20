def greet(name):
    return "Hello, " + name + "!"


def add(a, b):
    # BUG: this subtracts instead of adding
    return a - b


if __name__ == "__main__":
    print(greet("world"))
    print(add(2, 3))
