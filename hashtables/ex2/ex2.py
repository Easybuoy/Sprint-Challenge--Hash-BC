#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in range(len(tickets)):
        # print(tickets[i])
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
        print(hash_table_retrieve(hashtable, tickets[i].source), tickets[i-1].source)
        # if (hash_table_retrieve(hashtable, tickets[i].source) ):
        route[i] = hash_table_retrieve(hashtable, tickets[i].source)

        # print(hash(tickets[i].source, tickets[i].destination))
    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3))
