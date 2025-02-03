# Define a list 'my_list' containing multiple numbers, including duplicates
my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

# Print the original list 'my_list'
print("Original List : ", my_list)

counter = {}


for i in my_list:
    if i in counter: # i 라는 key 가 counter 에 있다면
        counter[i] += 1
    else: # i 라는 key 가 counter 에 없다면
        counter[i] = 1

# # Print the frequency of the elements in the list, as provided by the 'ctr' object
# print("Frequency of the elements in the List : ", counter) 