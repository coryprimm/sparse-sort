#import sparseModule
from ..sparse import sparsedSort
import time
import random

randomArr = [random.randrange(0, 1000) for _ in range(1000000)]
# randomArr = [random.uniform(0, 100) for _ in range(100)]

deep_copy_array = randomArr[:]

deep_copy_array2 = randomArr[:]

def recordTime(function, arr, name):
	# Record the start time
	start_time = time.time()

	# Call your sorting function
	sorted_output = function(arr)

	# Record the end time
	end_time = time.time()

	# Calculate the elapsed time
	elapsed_time = end_time - start_time

	# Print the sorted output and the time taken
	# print("Sorted Output:", sorted_output)
	print("""Time Taken by {name}:""".format(name=name), elapsed_time, "seconds")
    # print("Sorted Output:", sorted_output)
	return [name,elapsed_time, sorted_output]



def builtInSort(arr):

    arr.sort()

    return arr

builtInPerformance = recordTime(builtInSort, deep_copy_array, 'Python\'s Built in Tim Sort')

def sparseModuleSort(arr):

    newarr = sparsedSort(arr)

    return newarr

modulePerformance = recordTime(sparseModuleSort, deep_copy_array2, 'Sparse Module Performance')


def sortFloatsByInteger(input_list):
    print("i am in the second function now")
    int_values = [int(num) for num in input_list]
    min_value = int(min(int_values))
    max_value = int(max(int_values))

    sorted_dict = {}

    for num in input_list:
        int_part = int(num)
        
        if int_part not in sorted_dict:
            sorted_dict[int_part] = []
        
        sorted_dict[int_part].append(num)

    sorted_list = []

    for num in range(min_value, max_value + 1):
        if num in sorted_dict:
            insertion_sort(sorted_dict[num])
            sorted_list.extend(sorted_dict[num])

    return sorted_list

def insertion_sort(L):
    for i, value in enumerate(L):
        for j in range(i - 1, -1, -1):
            if L[j] > value:
                L[j + 1] = L[j]
                L[j] = value
    return L

def customSort(input_arr):
    try:
        min_value = min(input_arr)
        max_value = max(input_arr)
        
        # Create a dictionary to represent the sparse array
        sparse_array = {}
        
        # Populate the sparse array
        for num in input_arr:
            if num in sparse_array:
                sparse_array[num] += 1
            else:
                sparse_array[num] = 1
        
        # Generate the sorted output
        sorted_output = []
        for num in range(min_value, max_value + 1):
            if num in sparse_array:
                sorted_output.extend([num] * sparse_array[num])
        
        return sorted_output
    except (ValueError, TypeError):
    # Handle the case where input_arr contains floats
        return sortFloatsByInteger(input_arr)

sparsePerformance = recordTime(customSort, randomArr, 'Sparse Sort in Python')



def comparePerformance(results):
    # Sort the results by execution time (fastest to slowest)
    sorted_results = sorted(results, key=lambda x: x[1])

    # for i in range(len(sorted_results)):
    #     name, elapsed_time, arr = sorted_results[i]
    #     print(arr)

    # Print the sorted results
    for i in range(len(sorted_results)):
        name, elapsed_time, arr = sorted_results[i]
        print(f"{name} was {i + 1} fastest in {elapsed_time:.10f} seconds")

comparePerformance([builtInPerformance, modulePerformance, sparsePerformance])
