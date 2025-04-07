import json
import os
from itertools import count

# get current working directory path
cwd_path = os.getcwd()

def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path,mode="r") as json_file:
        sequential_data = json.load(json_file)
    return sequential_data[field]

def linear_search(sequence:list, number):
    list_of_index = []
    count_index = 0
    index = 0
    while index < len(sequence):
        if sequence[index]==number:
            count_index += 1
            list_of_index.append(index)
        index += 1
    return {
        "position": list_of_index,
        "count": count_index
    }

def pattern_search(sequence:list, pattern):
    index_set = set()
    index = 0
    while index <= len(sequence) - len(pattern):
        if sequence[index : index+len(pattern)] == pattern:
            index_set.add(index)
        index+=1
    return index_set

def main():
    file_name = "sequential.json"

    seq = read_data(file_name, field="dna_sequence")
    print(seq)

    set_seq = pattern_search(seq,"GCA")
    print(len(seq))
    print(set_seq)

if __name__ == '__main__':
    main()