#Module is wrapped in this logic to handle errors
try:
    import sparseModule
    use_c_module = True
except ImportError:
    use_c_module = False

def sparsedSort(input_arr):
    if use_c_module:
        try:
            # Attempt to use the C module
            return sparseModule.sparseSort(input_arr)
        except:
            pass  # Handle exceptions from the C module, e.g., for floats
    return sorted(input_arr)
