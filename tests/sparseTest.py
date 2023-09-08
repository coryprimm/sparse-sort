#import sparseModule
from ..sparse import sparsedSort
from logicInPython import sortFloatsByInteger, insertion_sort, customSort
import time
import random

randomArr = [random.randrange(0, 1000) for _ in range(1000000)] 
# randomArr = [random.uniform(0, 100) for _ in range(100)] # To create floats

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

#sparsePerformance = recordTime(customSort, randomArr, 'Sparse Sort in Python')

def comparePerformance(results):
    # Sort the results by execution time (fastest to slowest)
    sorted_results = sorted(results, key=lambda x: x[1])

    # Print the sorted results
    for i in range(len(sorted_results)):
        name, elapsed_time, arr = sorted_results[i]
        print(f"{name} was {i + 1} fastest in {elapsed_time:.10f} seconds")

comparePerformance([builtInPerformance, modulePerformance, sparsePerformance])
