def get_data(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(int(line.removesuffix('\n')))
    return data


def get_max(array):
    return max(array)


def get_min(array):
    return min(array)


def get_median(array):
    temp = sorted(array)
    n = len(temp)
    if n % 2 == 0:
        median = (temp[n // 2 - 1] + temp[n // 2]) / 2
    else:
        median = temp[n // 2]
    return median


def get_average(array):
    return sum(array) / len(array)


def get_max_sequence(array, reverse=False):
    max_sequence = []
    current_sequence = [array[0]]

    for i in range(1, len(array)):
        if (reverse and array[i] < array[i - 1]) or (not reverse and array[i] > array[i - 1]):
            current_sequence.append(array[i])
        else:
            if len(current_sequence) > len(max_sequence):
                max_sequence = current_sequence
            current_sequence = [array[i]]

    if len(current_sequence) > len(max_sequence):
        max_sequence = current_sequence

    return max_sequence


numbers = get_data("10m.txt")
print(f"Max: {get_max(numbers)}")
print(f"Min: {get_min(numbers)}")
print(f"Median: {get_median(numbers)}")
print(f"Average: {round(get_average(numbers), 2)}")
print(f"Max asc sequence: {get_max_sequence(numbers)}")
print(f"Max desc sequence: {get_max_sequence(numbers, reverse=True)}")
