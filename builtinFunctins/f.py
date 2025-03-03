def all_true(elements):
    return all(elements)

tuple1 = (True, True, False, True)
tuple2 = (True, True, True)

print("All elements in tuple1 are true:", all_true(tuple1))
print("All elements in tuple2 are true:", all_true(tuple2))