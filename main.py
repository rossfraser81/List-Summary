print ("\t\t\t\tSummary Table")

#create string list, print class, elements and class of first element

num_strings = ["53","45","77","100"]
print("\nThe variable num_strings is a " + str(type(num_strings)) + ".")
print("It contains the elements: " + str(num_strings))
print("The element " + num_strings[0] + " is a " + str(type(num_strings[0])) + ".")

#create int list, print class, elements and class of first element

num_ints = [53,45,77,100]
print("\nThe variable num_ints is a " + str(type(num_ints)) + ".")
print("It contains the elements: " + str(num_ints))
print("The element " + str(num_ints[0]) + " is a " + str(type(num_ints[0])) + ".")

#create float list, print class, elements and class of first element

num_floats = [53.5,45.8,77.77777,100.135986]
print("\nThe variable num_floats is a " + str(type(num_floats)) + ".")
print("It contains the elements: " + str(num_floats))
print("The element " + str(num_floats[0]) + " is a " + str(type(num_floats[0])) + ".")

#create list of lists, print class, elements and class of first element

num_lists = [[1,2,3],[4,5,6],[7,8,9]]
print("\nThe variable num_lists is a " + str(type(num_lists)) + ".")
print("It contains the elements: " + str(num_lists))
print("The element " + str(num_lists[0]) + " is a " + str(type(num_lists[0])) + ".")

#sort strings and ints

print("\nSorting num_strings and num_ints...")
num_strings.sort()
print("Sorted num_strings: " + str(num_strings))
num_ints.sort()
print("Sorted num_ints: " + str(num_ints))

print("\nStrings are sorted alphabetically while integers are sorted numerically.")




