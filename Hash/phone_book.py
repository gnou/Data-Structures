# python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def search(self, k):
        p = self.head
        if p != None:
            while p.next != None:
                if (p.data == k):
                    return p
                p = p.next
            if (p.data == k):
                return p
        return None

    def remove(self, p):
        tmp = p.prev
        p.prev.next = p.next
        p.prev = tmp

    def __str__(self):
        s = ""
        p = self.head
        if p != None:
            while p.next != None:
                s += p.data
                p = p.next
            s += p.data
        return s


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def hash_int(n):
    p = 10 ** 7 + 19
    a = 89
    b = 23
    m = 1000
    hash = ((a * n + b) % p) % m
    return hash


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else:  # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result


def process_queries2(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    m = 1000  # init hash table size
    contacts = [None] * m

    for cur_query in queries:
        hash_num = hash_int(cur_query.number)

        if cur_query.type == 'add':
            node = Node(cur_query)
            root = contacts[hash_num]
            if root is None:
                contacts[hash_num] = node
            else:
                a_node = root
                is_used = False
                while a_node is not None:
                    if a_node.value.number == cur_query.number:
                        a_node.value.name = cur_query.name
                        is_used = True
                        break
                    a_node = a_node.next

                if not is_used and a_node is None:
                    a_node.next = node

        elif cur_query.type == 'del':
            contacts[hash_num] = None
            # root = contacts[hash_num]
            # if root is not None:
            #     a_node = root
            #     while a_node.next is not None:
            #         if a_node.value.number == cur_query.number:
        else:
            response = 'not found'
            # for contact in contacts:
            #     if contact.number == cur_query.number:
            #         response = contact.name
            #         break
            # result.append(response)
            contact = contacts[hash_num]
            if contact is not None and contact.number == cur_query.number:
                response = contact.name
            result.append(response)

    return result


def process_queries3(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = [None] * 10 ** 7
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            # for contact in contacts:
            #     if contact.number == cur_query.number:
            #         contact.name = cur_query.name
            #         break
            # else: # otherwise, just add it
            #     contacts.append(cur_query)
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            contacts[cur_query.number] = None
            # for j in range(len(contacts)):
            #     if contacts[j].number == cur_query.number:
            #         contacts.pop(j)
            #         break
        else:
            response = 'not found'
            # for contact in contacts:
            contact = contacts[cur_query.number]
            if contact is not None:
                response = contact
                # break
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries3(read_queries()))
