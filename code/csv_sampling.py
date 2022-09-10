import random

def csv_sampling(dict):
    key_list = list(dict.keys())
    if len(key_list)> 10:
        key_list = list(dict.keys())
        sample_size = random.randint(5, 10)
        sample_keylist_index = random.sample(range(0, len(key_list)), sample_size)
        sample_keys = []
        for i in sample_keylist_index:
            sample_keys.append(key_list[i])
        sample_dict = {}
        for i in sample_keys:
            sample_dict[i] = dict[i]
    return sample_dict


