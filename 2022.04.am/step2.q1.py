from typing import List


def find_anagram_sets(word_list: List[str]) -> List[List[str]]:
    """
    Finds anagram sets for a given word list.

    Complexity: W_C = word_count, L = word_length
    O(L*N + N*N)

    :param word_list: list of words
    :return: list of anagram sets
    """
    frequency_map_list = []
    for word in word_list:
        frequency_map = create_frequency_map(word)
        frequency_map_list.append(frequency_map)

    anagram_set_list = [[0]]
    for word_index in range(1, len(word_list)):
        fit_in_an_anagram_set = False
        for anagram_set in anagram_set_list:
            first_word_index = anagram_set[0]
            if frequency_map_list[word_index] == frequency_map_list[first_word_index]:
                anagram_set.append(word_index)
                fit_in_an_anagram_set = True

        if not fit_in_an_anagram_set:
            anagram_set = [word_index]
            anagram_set_list.append(anagram_set)

    anagram_word_lists = [[word_list[index] for index in anagram_set] for anagram_set in anagram_set_list]

    return anagram_word_lists


def create_frequency_map(word: str) -> List[int]:
    frequency_map = [0] * 32
    for char in word:
        index = find_alphabet_order(char)
        frequency_map[index] += 1
    return frequency_map


def find_alphabet_order(character: str) -> int:
    """
    Finds index of a chracter in the alphabet
    """
    char_ord = ord(character)
    if char_ord >= 97:
        return char_ord - 97
    else:
        return char_ord - 65


if __name__ == '__main__':
    word_list = ["ali", "veli", "stop", "post", "deli", "pak", "kap"]
    print(find_anagram_sets(word_list))
