#ifndef SPARSESORT_H
#define SPARSESORT_H

#include <stdbool.h> // Include the standard bool library

// Function prototype for checking if an array contains floats
bool containsFloats(int arr[], int size);

// Function prototypes
int findMin(int arr[], int size);
int findMax(int arr[], int size);
int* sparseSort(int input_arr[], int size, int* sorted_size);

#endif