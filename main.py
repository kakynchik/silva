def filter_python_strings(strings):
    filtered_strings = []
    for string in strings:
        if "Python" in string:
            filtered_strings.append(string)
    return filtered_strings
input_strings = input("vvedit ryadki(z probelami): ").split()
filtered_list = filter_python_strings(input_strings)
print("spiski ryadkov s 'Python':", filtered_list)
