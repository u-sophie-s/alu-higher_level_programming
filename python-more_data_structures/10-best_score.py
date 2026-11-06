#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_key = None
    highest_score = 0

    for key in a_dictionary:
        if a_dictionary[key] > highest_score:
            highest_score = a_dictionary[key]
            best_key = key

    return best_key
