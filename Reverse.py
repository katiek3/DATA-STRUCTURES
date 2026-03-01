"""Revserse List to String"""
def reverse_list_string(data: list[str], tab_by: int) -> str | None:
    if data is None or len(data) == 0:
        return None
    NEWLINE = "\n"
    string = ""
    indent = 0

    for item in data:
        if string == "": 
            string = item 
        else:
            string = item + NEWLINE + (" " * indent) + string
        indent += tab_by
    return string

data = ['Howard', 'Jarvis', 'Morse', 'Loyola']
tab_by = 2
result = reverse_list_string(data, tab_by)
print(result)


""" Compare List Content """
def measure_similarity(target: list[str], reference: list[str]) -> float:
    if not target:
        return 0.0
    matches = 0 
    for element in target:
        if element in reference:
            matches += 1
    similarity = matches / len(target)
    return similarity
target1 = ['apple', 'banana', 'pear', 'kiwi']
reference1 = ['banana', 'kiwi', 'grape', 'orange']
similarity = measure_similarity(target1, reference1)
print (similarity)

"""Compare List Comparison"""
def measure_similarity(target : list[str], reference: list[str]) -> float:
    ref_set = set(reference)
    matches = 0
    for x in target:
        if x in ref_set:
            matches += 1
    TARGET_DENOMINATOR = 1
    
    if len(target) > 0:
        denominator = len(target)
    else:
        denominator = TARGET_DENOMINATOR
    return matches / denominator
                                 
def report_similarity(target: list[str], reference: list[str]) -> str:  
    s = measure_similarity(target, reference)
    return f"{s*100:.2f}%"
target = ['a', 'b', 'c', 'd']
reference = ['c', 'd', 'e', 'f']
print (report_similarity(target, reference))

"""Count Frequencies"""
def efficient_frequency_counter(message: str) -> list[int]:
    LETTERS = "abcdefghijklmnopqrstuvwxyz"
    NUMEBR_OF_LETTERS = len(LETTERS)
    SPACE_INDEX = NUMEBR_OF_LETTERS
    TOTAL_CHARACTERS = NUMEBR_OF_LETTERS + 1
    frequency = [0] * TOTAL_CHARACTERS

    for char in message:
        if char == ' ':
            frequency[SPACE_INDEX] += 1
        else:
            i = 0 
            while LETTERS[i] != char:
                i += 1
            frequency[i] += 1
    return frequency
pangram = "sphinx of black quartz judge my vow"
result = efficient_frequency_counter(pangram)
print(result)

def simple_frequency_counter(message: str) -> dict[str, int]:
    frequency = {}
    if message is not None and len(message) > 0:
        for char in message:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency
pangram = "sphinx of black quartz judge my vow"
result = simple_frequency_counter(pangram)
print(result)

""""Test for Count Frequencies"""
import sys # to check memory usage
pangram = "sphinx of black quartz judge my vow"
dict_freq = simple_frequency_counter(pangram) # method provided above
list_freq = efficient_frequency_counter(pangram) # your method
print(sys.getsizeof(dict_freq), "bytes for dict")
print(sys.getsizeof(list_freq), "bytes for list")





