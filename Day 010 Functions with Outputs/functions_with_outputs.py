# Functions with Outputs

def my_function():
    """
    This function will return a number.
    """
    return 3 * 2


def format_name(f_name, l_name):
    """
    This function will return a formatted name in Title Case.
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    # print(f"{formated_f_name} {formated_l_name}")
    return f"{formated_f_name} {formated_l_name}"


#output = my_function()
# print(type(output))
print(format_name("PaUL", "WaTtS"))

print(len(format_name("PaUL", "WaTtS")))
