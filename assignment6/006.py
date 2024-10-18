def swap(string):
    first = string[0]
    last = string[-1]
    swapped_string = last + string[1:-1] + first
    print(swapped_string)

swap('Thank you')