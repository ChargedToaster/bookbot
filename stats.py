def word_number(book_text):
    num_words = len(book_text.split())
    return num_words

def character_count(book_text):
    freq_dict = {}
    for char in book_text.lower():
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

def sort_list(freq_dict):
    sorted_list = []

    for char, count in freq_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(key=lambda item: item["num"], reverse=True)
    return sorted_list

