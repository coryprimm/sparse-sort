#include <Python.h>
#include "sparseSort.h"

// Python method to call the custom sorting function
static PyObject* sparse_sort(PyObject* self, PyObject* args) {
    PyObject* py_list;
    if (!PyArg_ParseTuple(args, "O", &py_list)) {
        return NULL;
    }

    // Check if the input is a list
    if (!PyList_Check(py_list)) {
        PyErr_SetString(PyExc_TypeError, "Input must be a list.");
        return NULL;
    }

// Convert the Python list to a C array
    Py_ssize_t size = PyList_Size(py_list);
    if (size == -1) {
        PyErr_SetString(PyExc_RuntimeError, "Failed to get list size.");
        return NULL;
    }

    int* input_arr = (int*)malloc(size * sizeof(int));
    if (input_arr == NULL) {
        PyErr_SetString(PyExc_MemoryError, "Memory allocation failed.");
        return NULL;
    }

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject* item = PyList_GetItem(py_list, i);
        if (!PyLong_Check(item)) {
            PyErr_SetString(PyExc_TypeError, "List must contain integers.");
            free(input_arr);
            return NULL;
        }
        input_arr[i] = PyLong_AsLong(item);
    }

    int sorted_size;
    int* sorted_output = sparseSort(input_arr, size, &sorted_size);

    // Convert the result back to a Python list
    PyObject* sorted_list = PyList_New(sorted_size);
    if (sorted_list == NULL) {
        PyErr_SetString(PyExc_RuntimeError, "Failed to create a new list.");
        free(input_arr);
        free(sorted_output);
        return NULL;
    }

    for (int i = 0; i < sorted_size; i++) {
        PyObject* py_num = PyLong_FromLong(sorted_output[i]);
        if (py_num == NULL) {
            PyErr_SetString(PyExc_RuntimeError, "Failed to convert to Python integer.");
            Py_DECREF(sorted_list);
            free(input_arr);
            free(sorted_output);
            return NULL;
        }
        PyList_SetItem(sorted_list, i, py_num);
    }

    free(input_arr);
    free(sorted_output);

    return sorted_list;
}

// Define the method mapping
static PyMethodDef methods[] = {
    {"sparseSort", sparse_sort, METH_VARARGS, "Custom sorting function"},
    {NULL, NULL, 0, NULL}
};

// Define the module structure
static struct PyModuleDef sparseModule = {
    PyModuleDef_HEAD_INIT,
    "sparseModule",  // Module name
    NULL,      // Module documentation
    -1,        // Size of per-interpreter state of the module
    methods    // Method mapping
};

// Module initialization function
PyMODINIT_FUNC PyInit_sparseModule(void) {
    return PyModule_Create(&sparseModule);
}
