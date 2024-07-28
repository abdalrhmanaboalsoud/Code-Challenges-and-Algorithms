# Whiteboard Diagram for Sum of Unique Elements

## 1. Problem Domain

### Description
The task is to compute the sum of unique elements in an array. Unique elements are those that appear exactly once in the array.

### Example
- **Input:** `[1, 2, 3, 2]`
- **Output:** `4` (since `1` and `3` are unique, and their sum is `4`)

## 2. Algorithms

### Overview
1. **Linked List Construction**: Build a linked list from the array elements.
2. **Frequency Counting**: Use a hash table (dictionary) to count occurrences of each element in the linked list.
3. **Sum Calculation**: Iterate over the frequency count to sum up elements that appear exactly once.

### Detailed Steps
1. **Construct Linked List**:
   - Initialize a linked list.
   - Append each element of the array to the linked list.

2. **Count Elements**:
   - Traverse the linked list.
   - Use a dictionary to count occurrences of each element.

3. **Sum Unique Elements**:
   - Iterate over the dictionary.
   - Sum the elements that have a count of `1`.

## 3. Pseudo Code

### Function: `sum_of_unique_elements(nums)`

1. **Initialize** `linked_list`
    - For each `num` in `nums`:
        - `linked_list.append(num)`
2. **Initialize** `element_count` as an empty dictionary
    - For each `data` in `linked_list`:
        - If `data` is in `element_count`:
            - Increment `element_count[data]`
        - Else:
            - Set `element_count[data]` to 1
3. **Initialize** `unique_sum` as 0
    - For each `element, count` in `element_count`:
        - If `count` is 1:
            - Add `element` to `unique_sum`
4. **Return** `unique_sum`

## 4. Test Cases

| Test Case | Input                     | Expected Output | Explanation                                                   |
|-----------|---------------------------|-----------------|---------------------------------------------------------------|
| 1         | `[1, 2, 3, 2]`            | `4`             | Unique elements are `1` and `3`. Sum = `1 + 3 = 4`.          |
| 2         | `[1, 2, 3, 4, 5]`         | `15`            | All elements are unique. Sum = `1 + 2 + 3 + 4 + 5 = 15`.    |
| 3         | `[1, 1, 2, 2, 3, 3]`      | `0`             | No unique elements. Sum = `0`.                               |
| 4         | `[]`                      | `0`             | Empty array. Sum = `0`.                                     |
| 5         | `[10]`                    | `10`            | Only one element, which is unique. Sum = `10`.               |
| 6         | `[1000, 2000, 3000, 1000]`| `5000`          | Unique elements are `2000` and `3000`. Sum = `2000 + 3000`.  |
| 7         | `[4, 5, 6, 4, 7, 8, 9, 5, 6, 10]` | `34` | Unique elements are `7, 8, 9, 10`. Sum = `7 + 8 + 9 + 10`.  |

## 5. Big O Notation

- **Time Complexity**: `O(n)`
  - Constructing the linked list: `O(n)`
  - Counting elements: `O(n)`
  - Summing unique elements: `O(n)`
  - Overall: `O(n)`, where `n` is the number of elements in the input array.

- **Space Complexity**: `O(n)`
  - Space for the linked list: `O(n)`
  - Space for the hash table: `O(n)`
  - Overall: `O(n)`

