def count_occurrences(sample_list):
    count_dict = {}
    for item in sample_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

# Test the function
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
occurrence_count = count_occurrences(sample_list)
print("Printing count of each item:", occurrence_count)
