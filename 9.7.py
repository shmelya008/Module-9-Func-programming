def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        div = 0
        for i in range(2, result):
            if result % i == 0:
                div += 1
        if div <= 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper


@is_prime
def sum_three(*args):
    res_ = sum(args)
    return res_


result = sum_three(2, 3, 6)
print(result)
