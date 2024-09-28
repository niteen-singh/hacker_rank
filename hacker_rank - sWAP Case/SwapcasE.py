def swap_case(text_input):
    str_output = ""
    for char in text_input:
        if char.islower():
            str_output +=char.upper()
        elif char.isupper():
            str_output +=char.lower()
        else:
            str_output +=char
    return str_output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)