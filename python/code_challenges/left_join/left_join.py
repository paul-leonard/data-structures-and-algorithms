'''
Required Features:
- [x] Write a function that LEFT JOINs two hashmaps into a single data structure.
- [x] The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
- [x] The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
- [x] Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
- [x] LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row. If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.
- [x] The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic.
- [x] Avoid utilizing any of the library methods available to your language.
'''

def left_join(hashtable_left, hashtable_right):

    output = []
    for bucket in hashtable_left._buckets:
        if bucket:
            current = bucket.head
            while current:
                current_key = current.value[0]
                current_value = current.value[1]

                this_set = [current_key,current_value]

                if hashtable_right.contains(current_key):
                    this_set.append(hashtable_right.get(current_key))
                else:
                    this_set.append(None)

                output.append(this_set)
                current = current.next_node

    return output

def right_join(hashtable_right, hashtable_left):
    return left_join(hashtable_right, hashtable_left)
