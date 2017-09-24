def build_freq_table(input_str):
    freq_dict={}

    for c in input_str:
        if c in freq_dict:
            cur_freq = freq_dict[c]
            freq_dict[c] = cur_freq + 1
        else:
            freq_dict[c] = 1
    return freq_dict

def main():
    my_string = 'somebody_once_told_me_the_world_was_gonna_roll_me'
    my_frequency_table = build_freq_table(my_string)
    print(my_frequency_table)

if __name__ == "__main__" :
    main() 