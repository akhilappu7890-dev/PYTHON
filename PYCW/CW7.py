initial_items =['milk','bread','eggs']
def add_item(initial_items):
    initial_items.append("banana")
    print(initial_items)
add_item(initial_items)
    
def remove_last_item(initial_items):
    initial_items.pop(3)
    print(initial_items)
remove_last_item(initial_items)

print_item = lambda item: print('item',item)
for item in initial_items:
    print_item(item)
    
    def count_characters(initial_items):
        if initial_items == []:
            return 0
        return len(initial_items[0]) + count_characters(initial_items[1:])
    print('total charaters',count_characters(initial_items))