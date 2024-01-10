#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
    """
    print list in ascending sorted order.
    
    """
    sorted_list = sorted(self)
    print(sorted_list)
