def num_squared(num):
    squares = [i * i for i in range(num + 1)]
    return squares

if __name__ == "__main__":
    print(num_squared(10))
