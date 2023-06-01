def filter_capitalized_strings(strings):
    filtered_strings = []
    for string in strings:
        if string[0].isupper():
            filtered_strings.append(string)
    return filtered_strings
input_strings = input("vvedit ryadki(z probelami): ").split()
filtered_list = filter_capitalized_strings(input_strings)
print("ryadki s bolshoy bykvi:", filtered_list)