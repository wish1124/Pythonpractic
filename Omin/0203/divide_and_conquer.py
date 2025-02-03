#Merge Sort


def merge(left, right):
  merged = []
  i = j = 0
  
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1
      
  if i == len(left):
    merged.extend(right[j:])
  else:
    merged.extend(left[i:])
    
  return merged



def merge_sort(arr):
  if len(arr) == 1:
    return arr
  
  mid = len(arr) // 2
  
  left_half = merge_sort(arr[:mid])
  right_half = merge_sort(arr[mid:])
  
  x = merge(left_half, right_half)
  
  return x
  
array = [38, 27 , 43, 13, 9, 82, 10]

sorted_array = merge_sort(array)

print(sorted_array)