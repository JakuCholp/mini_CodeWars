

def create_function_string(name_function, count_arg):
    argument_list = ", ".join([f"arg{i}" for i in range(1, count_arg + 1)])
    function_string = f"{name_function}({argument_list}):"
    return function_string