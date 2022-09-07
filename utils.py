def find_max(lists):
    high = lists[0]    
    for large in lists:
        if large > high:
            high = large
    return high
    