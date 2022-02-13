
def element_ranking(seq):
    sorted_seq = sorted(seq, reverse = True)
    ranked = []
    for element in seq:
        ranked_index = sorted_seq.index(element)
        ranked.append(ranked_index + 1)
    return ranked


def test_element_ranking():
    

    #assert element_ranking([]) == []
    assert element_ranking([0]) == [1]
    assert element_ranking([3,3]) == [1,1]
    assert element_ranking((2,4)) == [2,1]
    assert element_ranking((4,2)) == [1,2]
    assert element_ranking((10, 4, 7, -1)) == [1, 3, 2, 4]
    assert element_ranking((10.1, 99.0, 93, 51, 93)) == [5, 1, 2, 4, 2]
    assert element_ranking([10.1, 51, 99.0, 93, 51, 99.0, 51]) == [7, 4, 1, 3, 4, 1, 4]

    print("all tests passed")

if __name__ == "__main__":
    test_element_ranking()

