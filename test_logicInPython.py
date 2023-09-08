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