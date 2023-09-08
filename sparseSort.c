#include <stdio.h>
#include <stdlib.h>

// sparseSort.c
#include "sparseSort.h"

#include <stdbool.h> 

// Helper function to check if an array contains floats
bool containsFloats(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        if (arr[i] % 1 != 0) {
            return true;
        }
    }
    return false;
}

int findMin(int arr[], int size) {
    int min = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    return min;
}

int findMax(int arr[], int size) {
    int max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

int* sparseSort(int input_arr[], int size, int* sorted_size) {

        if (containsFloats(input_arr, size)) {
        // For simplicity, let's raise an error here:
        fprintf(stderr, "Error: Input contains floats. This sorting algorithm only works with integers.\n");
        exit(1); // Exit the program with an error code
    }

    int min_value = findMin(input_arr, size);
    int max_value = findMax(input_arr, size);
    
    // Create an array to represent the sparse array
    int* sparse_array = (int*)malloc((max_value - min_value + 1) * sizeof(int));
    
    // Initialize the sparse array with zeros
    for (int i = 0; i < max_value - min_value + 1; i++) {
        sparse_array[i] = 0;
    }
    
    // Populate the sparse array
    for (int i = 0; i < size; i++) {
        sparse_array[input_arr[i] - min_value]++;
    }
    
    // Calculate the size of the sorted output
    *sorted_size = 0;
    for (int i = 0; i < max_value - min_value + 1; i++) {
        *sorted_size += sparse_array[i];
    }
    
    // Generate the sorted output
    int* sorted_output = (int*)malloc(*sorted_size * sizeof(int));
    int index = 0;
    for (int num = min_value; num <= max_value; num++) {
        while (sparse_array[num - min_value] > 0) {
            sorted_output[index++] = num;
            sparse_array[num - min_value]--;
        }
    }
    
    free(sparse_array);
    return sorted_output;
}