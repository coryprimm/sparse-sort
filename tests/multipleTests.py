import random
import time
import numpy as np
from scipy.stats import skew, kurtosis, norm, percentileofscore
import secrets
from ..sparse import sparsedSort



score = { 'asCount': {'sparse': 0, 'builtIn':0},
'asAv': 0,
'runs': 0}

print(score['asCount'])

def analyze_distribution(data):
    # Compute basic statistics
    mean = np.mean(data)
    median = np.median(data)
    variance = np.var(data)
    std_deviation = np.std(data)
    
    # Compute skewness and kurtosis
    skewness = skew(data)
    kurt = kurtosis(data)
    
    # Compute percentiles
    percentiles = [25, 50, 75]
    percentile_values = np.percentile(data, percentiles)
    
    # Fit a normal distribution (if applicable)
    try:
        params = norm.fit(data)
        norm_mean, norm_std = params
        is_normal = True
    except Exception as e:
        is_normal = False
    
    # Calculate the empirical distribution function (EDF)
    sorted_data = np.sort(data)
    edf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
    
    # Create a dictionary to store the results
    results = {
        "Mean": mean,
        "Median": median,
        "Variance": variance,
        "Standard Deviation": std_deviation,
        "Skewness": skewness,
        "Kurtosis": kurt,
        "Percentiles": dict(zip(percentiles, percentile_values)),
        "Is Normal Distribution": is_normal,
        "Empirical Distribution Function": edf
    }
    print(results)

def manyRuns(num_of_runs, score):
    for j in range(0,num_of_runs):
        # randomArr = []
        # for i in range (0, 1000000):
        #     randomArr.append(random.randrange(0, 1000))

        #randomArr = [secrets.randbelow(1000) for _ in range(1000000)]  # Generates 10 random integers between 0 and 99


        # Parameters
        shape = 2  # Adjust this parameter to control skewness
        scale = 1.0
        num_samples = 1000000  # Number of samples in the array

        # Generate random values from a skewed distribution
        skewed_values = np.random.gamma(shape, scale, num_samples)

        # Round the values to integers
        randomArr = np.round(skewed_values).astype(int)


        deep_copy_array = randomArr[:]

        thirdCopy = deep_copy_array[:]
        print("""




        """)

        analyze_distribution(thirdCopy)


        sparsePerformance = recordTime(sparseModuleSort, deep_copy_array, 'Sparse Sort')
        builtInPerformance = recordTime(builtInSort, randomArr, 'Python\'s Built in Tim Sort')
        compareTwoPerformance(sparsePerformance, builtInPerformance, score, j + 1)
        print(score)

    print('=====================================')
    print("""




        """)
    print('final summary:')


    if score['asAv'] < 0: 
        print('python\'s builtin timsort wins the overall average by ' + str(score['asAv']) + ' for ' + str(score['runs']))
    else: 
        print('sparse sort wins the average by ' + str(score['asAv']) + ' for ' + str(score['runs']))
    if score['asCount']['sparse'] > score['asCount']['builtIn']:
        print('sparse beat the head to head line ups ' + str(score['asCount']['sparse']) + ' to ' + str(score['asCount']['builtIn']))
    elif score['asCount']['sparse'] < score['asCount']['builtIn']:
         print('timsort won the head to head line ups ' + str(score['asCount']['builtIn']) + ' to ' + str(score['asCount']['sparse']))
    else:
        print('It was a tie: ' + str(score['asCount']['builtIn']) + ' to ' + str(score['asCount']['sparse']))

    return score



def builtInSort(arr):

    arr.sort()

    return arr



def sparseModuleSort(arr):

    newarr = sparsedSort(arr)

    return newarr



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
	return [name,elapsed_time]

def compareTwoPerformance(arr1, arr2, score, runNumber):

    runNumber = runNumber + 1

    diff = abs(arr1[1] - arr2[1])
    diffUnAv = -1 * (arr1[1] - arr2[1])
    score['runs'] = score['runs'] + 1
    if arr1[1] > arr2[1]:
        print(arr2[0] + ' was faster than ' + arr1[0] + ' by ' + str(diff) + ' seconds') 
        print(score)
        score['asCount']['builtIn'] = score['asCount']['builtIn'] + 1
        score['asAv'] = (score['asAv'] * (runNumber - 1) + diffUnAv) / runNumber
        return score
    score['asCount']['sparse'] = score['asCount']['sparse'] + 1
    score['asAv'] = (score['asAv'] * (runNumber - 1) + diffUnAv) / runNumber
    print(arr1[0] + ' was faster than ' + arr2[0] + ' by ' + str(diff) + ' seconds')
    return score  

manyRuns(3, score)

# Example usage:
# data = np.random.normal(0, 1, 1000)  # Replace with your dataset

