def apply_all_func(int_list: (int, float), *functions):
    results = {}
    values = []
    keys = []
    for function in functions:
        values.append(function(int_list))
        keys.append(function.__name__)
    for i in range(len(keys)):
        results.update({keys[i]: values[i]})
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
