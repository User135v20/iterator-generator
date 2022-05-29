def fib_num_generator(first_num, second_num):
    while True:
        yield first_num
        first_num, second_num = second_num, first_num + second_num


def main():
    fib_num = fib_num_generator(0, 1)

    for i in range(100):
        print(next(fib_num))

if __name__ == '__main__':
    main()
