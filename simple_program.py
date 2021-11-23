# Create a simple program to practice using git

def remove_duplicates(a_list):
    '''Takes a list of elements and removes any duplicates so that each elelement 
    only appears at most once in the resulting list. a_list must be a list. '''


    # Convert a_list to a set to remove duplicates
    a_set = set(a_list)

    # Convert back to a list
    dedupe_list = list(a_set)

    return dedupe_list


age_of_competitors = [22,26,32,55,28,26,19,30,30, 30]

print(f"We have competitors of the following ages in our competition {sorted(remove_duplicates(age_of_competitors))}")


