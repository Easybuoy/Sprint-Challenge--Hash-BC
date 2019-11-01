#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    # ht = HashTable(16)
    """
    YOUR CODE HERE
    """
    response = []
    index = 0
    hash_table = HashTable(length)


    for i in range(len(weights)):
        hash_table_insert(hash_table, weights[i], i)

    while index < length:
        difference = limit - weights[index]
        print(difference)
        for i in range(len(weights)):
            if (weights[i] == difference):
                response.append(hash_table_retrieve(hash_table, weights[i]))

        index += 1

    if len(response) == 0:
        return None
    return response


print(get_indices_of_item_weights([9], 1, 9))
# print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
