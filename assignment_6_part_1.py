import random
import time

def deterministic_kth_smallest(input, k):
    # median of medians only works if we can divide the input
    # into groups of 5, so in case our input is of size less than 5
    # then we just return the kth smallest element by 
    if len(input) <= 5:
        return sorted(input)[k - 1]
    
    # split input array into chunks of 5 groups
    chunks = [input[x : x + 5] for x in range(0, len(input), 5)]
    # find medians
    medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]

    # find median of medians
    pivot = deterministic_kth_smallest(medians, (len(medians) // 2) + 1)

    # split input array based off of pivot value
    lower = [x for x in input if x < pivot]
    equal = [x for x in input if x == pivot]
    higher = [x for x in input if x > pivot]

    if k <= len(lower):
        return deterministic_kth_smallest(lower, k)
    elif k <= len(lower) + len(equal):
        return pivot
    else:
        return deterministic_kth_smallest(higher, k - len(lower) - len(equal))

def randomized_kth_smallest(input, k):
    # if input is of size 1 this is the base case
    # and we can simply return the first value
    if len(input) == 1:
        return input[0]
    
    # randomly choose a pivot vlaue
    pivot = random.choice(input)

    # split input array based off of pivot value
    lower = [x for x in input if x < pivot]
    equal = [x for x in input if x == pivot]
    higher = [x for x in input if x > pivot]

    if k <= len(lower):
        return deterministic_kth_smallest(lower, k)
    elif k <= len(lower) + len(equal):
        return equal
    else:
        return deterministic_kth_smallest(higher, k - len(lower) - len(equal))

# generate random data based on set input size
def generate_random_data(size):
    out = [random.randint(0, size) for x in range(size)]
    return out

# generate sorted data based on set input size
def generate_sorted_data(size):
    out = list(range(size))
    return out

# generate reversed sorted data based on set input size
def generate_reversed_sorted_data(size):
    out = list(range(size, 0, -1))
    return out

def part_1_analysis():
    # run experiment for input data on varying sizes
    for size in (10000, 100000, 1000000):
        # generate random, sorted, and reversed sorted data
        random_data = generate_random_data(size)
        sorted_data = generate_sorted_data(size)
        reversed_sorted_data = generate_reversed_sorted_data(size)

        # set k to random value in range [1 -> size)
        k = random.randint(1, size)

        print("Executing test for input size " + str(size) + " and k set to " + str(k))

        # run deterministic algo on random data and capture time taken
        start_time = time.time()
        deterministic_kth_smallest(random_data, k)
        end_time = time.time()
        print("Applying deterministic algo to " + str(size) + " random elements took " + str(end_time - start_time))

        # run randomized algo on random data and capture time taken
        start_time = time.time()
        randomized_kth_smallest(random_data, k)
        end_time = time.time()
        print("Applying randomized algo to " + str(size) + " random elements took " + str(end_time - start_time))

        # run deterministic algo on sorted data and capture time taken
        start_time = time.time()
        deterministic_kth_smallest(sorted_data, k)
        end_time = time.time()
        print("Applying deterministic algo to " + str(size) + " sorted elements took " + str(end_time - start_time))

        # run randomized algo on sorted data and capture time taken
        start_time = time.time()
        randomized_kth_smallest(sorted_data, k)
        end_time = time.time()
        print("Applying randomized algo to " + str(size) + " sorted elements took " + str(end_time - start_time))

        # run deterministic algo on reversed sorted data and capture time taken
        start_time = time.time()
        deterministic_kth_smallest(reversed_sorted_data, k)
        end_time = time.time()
        print("Applying deterministic algo to " + str(size) + " reversed sorted elements took " + str(end_time - start_time))

        # run randomized algo on reversed sorted data and capture time taken
        start_time = time.time()
        randomized_kth_smallest(reversed_sorted_data, k)
        end_time = time.time()
        print("Applying randomized algo to " + str(size) + " reversed sorted elements took " + str(end_time - start_time))
        print()
    


if __name__ == "__main__":
    part_1_analysis()