def rehash(oldhash, table_size):
    return (oldhash+1) % table_size

def weighted_ord_hash(string, table_size):
    hash_val = 0
    for position in range(len(string)):
        hash_val = hash_val + (ord(string[position]) * position)
    return hash_val % table_size


def perfectHash(item_list, table_size):
    
    perfectHast_table = dict([(i,None) for i,x in enumerate(range(table_size))])
    
    for item in item_list:
        i = weighted_ord_hash(item, table_size)
        print("%s hashed == %s \n" %(item, i))
        if perfectHast_table[i] == None:
            perfectHast_table[i] = item
        elif perfectHast_table[i] != None:
            print("Collision, attempting linear probe \n")
            next_slot = rehash(i, table_size)
            print("Setting next slot to %s \n" % next_slot)
            while perfectHast_table[next_slot] != None:
                next_slot = rehash(next_slot, len(perfectHast_table.keys()))
                print("Slot was not empty, trying next slot %s \n" % next_slot)
            if perfectHast_table[next_slot] == None:
                perfectHast_table[next_slot] = item
    return perfectHast_table


names = ["Josh", "Elena", "Yadi", 
         "Maria", "Anna", "George",
        "Bob", "Greg", "Gary", "Mike", "Marla"]

print(perfectHash(names, 11))