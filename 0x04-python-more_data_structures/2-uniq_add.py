#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_intergers = set()
    for element in my_list:
        unique_intergers.add(element)
        result = sum(unique_intergers)

        return result
