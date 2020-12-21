# Data Structures and Algorithms

## Language: `Python`


-----------------------------------------------------------------

# Hashtable Data Structure (Code Challenge 30)
Create a class for Hashtable that contains the methods of add, get, contains, and hash.

## Challenge
<!-- Given input of an integer array, the left index value, and the right index value, output an integer array of the same values sorted in ascending order through the use of a quick sort algorithm. -->

## Approach & Efficiency
<!-- A set of recursive functions are used to select a pivot value and compare each other value in the list againist it.  Repeated swapping of values occurs until all values that are less than the pivot value are placed to the left of the pivot value.  Also, any value greater than the pivot value is placed to the right of the pivot value.

This approach has a time complexity of O(nlog(n)) which is better than the insertion sort algorithm.  As for memory, the Big O is considered O(1) because the array is sorted in-place.  However, techinically it is O(log^2(n)) because of recursive function calls. -->

## Solution
[whiteboard](???)

## Sources
- some tests were supplied by JB
- [skipping pytests](https://docs.pytest.org/en/latest/skipping.html)
- [ord function](https://www.geeksforgeeks.org/ord-function-python/)



-----------------------------------------------------------------
Note:  Code Challenge 29 was a mock interview over merge_sort and quick_sort.
-----------------------------------------------------------------


# Quick Sorting of Integer List (Code Challenge 28)
Write a function that sorts a given integer array in ascending order.

## Challenge
Given input of an integer array, the left index value, and the right index value, output an integer array of the same values sorted in ascending order through the use of a quick sort algorithm.

## Approach & Efficiency
A set of recursive functions are used to select a pivot value and compare each other value in the list againist it.  Repeated swapping of values occurs until all values that are less than the pivot value are placed to the left of the pivot value.  Also, any value greater than the pivot value is placed to the right of the pivot value.

This approach has a time complexity of O(nlog(n)) which is better than the insertion sort algorithm.  As for memory, the Big O is considered O(1) because the array is sorted in-place.  However, techinically it is O(log^2(n)) because of recursive function calls.

## Solution
[Blog Post Explanation](code_challenges/quick_sort/BLOG)
[whiteboard](code_challenges/quick_sort/quick_sort_whiteboard.png)

## Sources
- Thanks to Ryan P. for our collaborative work on the whiteboard.
- [baseCS QuickSort Part 1](https://medium.com/basecs/pivoting-to-understand-quicksort-part-1-75178dfb9313)
- [baseCS QuickSort Part 2](https://medium.com/basecs/pivoting-to-understand-quicksort-part-2-30161aefe1d3)
- [Visualization of Quick Sort](https://www.youtube.com/watch?v=vxENKlcs2Tw)
- [GeeksForGeeks Quick Sort](https://www.geeksforgeeks.org/python-program-for-quicksort/)

-----------------------------------------------------------------

# Merge Sorting of Integer List (Code Challenge 27)
Write a function that sorts a given integer array in ascending order.

## Challenge
Given input of an integer array, output an integer array of the same values sorted in ascending order through the use of a merge sort algorithm.

## Approach & Efficiency
A recursive function is used to divide each integer array argument in half and then merge them back together in a sorted fashion.  Each half of an array is then divided in half again when the same function is recursively called on it.

This approach has a time complexity of O(nlog(n)) which is better than the insertion sort algorithm.  As for memory, the Big O is O(n) because the array is temporarily stored in out-of-place memory.

## Solution
[Blog Post Explanation](code_challenges/merge_sort/BLOG)

## Sources
- Thanks to Mark Bell for our collaborative work on the whiteboard and troubleshooting issues.
- [basecs merge sort part 1](https://medium.com/basecs/making-sense-of-merge-sort-part-1-49649a143478)
- [basecs merge sort part 2](https://medium.com/basecs/making-sense-of-merge-sort-part-2-be8706453209)


-----------------------------------------------------------------

# Insertion Sorting of Integer List (Code Challenge 26)
Write a function that sorts a given integer array in ascending order.

## Challenge
Given input of an integer array, output an integer array of the same values sorted in ascending order through the use of an insertion sort algorithm.

## Approach & Efficiency
The array is divided into two groups using a for statement.  The fist group is the sorted portion of the array and the second half is unsorted.  As the for loop increments, the sorted portion of the array grows in size while the unsorted portion shrinks. An inner for loop finds the minimum value of the unsorted portion of the array and moves it to be the last value in the sorted portion of the array.  The function then returns the sorted array.

This approach requires a Big O(n^2) with regards to time because of the nested for loops running the full length of the array.  As for memory, the Big O is O(1) because the array is rearranged in place.

## Solution
[Blog Post Explanation](code_challenges/insertion_sort/BLOG)

## Sources
- [python range function](https://www.w3schools.com/python/ref_func_range.asp)


-----------------------------------------------------------------

# Breadth-First Method for Binary Tree Class (Code Challenge 18)
Produce a list of values stored in a binary tree in a breadth-first fashion.

## Challenge
Write a breadth first traversal method which takes a Binary Tree as its unique input. Without utilizing any of the built-in methods available to your language, traverse the input tree using a Breadth-first approach, and return a list of the values in the tree in the order they were encountered.

## Approach & Efficiency
A method was added to the BinaryTree class to print out the values stored in the tree in a breadth-first fashion.  A while loop and a Queue class data structure was used to provide the correct ordering of the node values.

This simple approach lead to a Big O(n) for time since each node had to be visited.  With regards to memory, the Big O was O(w) since the queue would build up with nodes equal to the width of the tree before a tree node was dequeued from the queue.

## Solution
[Picture of Whiteboard Exercise](code_challenges/Code_Challenge_18.png)


-----------------------------------------------------------------
# Max Numerical Value in Binary Tree (Code Challenge 17)
Find the maximum numerical value in a binary tree.

## Challenge
Write an instance method called find-maximum-value. Without utilizing any of the built-in methods available to your language, return the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Approach & Efficiency
A method was added to the BinaryTree superclass to allow for finding the maximum value in a binary tree.  The method uses a helper function, which it defines, to check the current node value againist the current_maximum and then recursively call any left or right nodes that node contains.  If the value of that node is larger than the current_maximum, then the current_maximum is assigned the value of the current node.  A nonlocal variable is used within the helper function that is initially set equal to the tree.root.value.

The process must step through each node, so the Big O with respect to time is O(n).  The data is not pulled from the binary tree, and only the current maximum is held in memory, so no new data structure is created.  However, the recursive calling of functions leads to a call stack that, at its max, becomes equal to the height of the tree.  Therefore, the Big O with respect to memory is O(h).

## Solution
[Picture of Whiteboard Exercise](code_challenges/Code_Challenge_17.png)


-----------------------------------------------------------------
# Animal Shelter (Code Challenge 12)
Come get a new dog or cat at our First In - First Out Animal Shelter!

## Challenge
Create a First In - First Out animal shelter making use of queues, classes, and objects.  Handle cats and dogs seperately and see who has been there the longest.

## Approach & Efficiency
A class was defined for the shelter.  It contained methods for adding animals of either dog or cat class to the shelter.  The shelter returns users their preference of cat or dog based on a first in, first out approach.  Two seperate queues are used to keep the cats and dogs in order and to prevent any dogs from chasing the cats.  Both cats and dogs are a subclass of the animal class.  If a visitor requests an animal and does not provide a preference, they are given the animal that has been in the shelter the longest.

## Solution
[Picture of Whiteboard Exercise](code_challenges/Code_Challenge_12.png)

-----------------------------------------------------------------

# PseudoQueues Using Stacks (Code Challenge 11)
Create a package defining classes for PseudoQueues to provide a structure for data, using Stacks and Nodes under the hood.

## Challenge
Create a brand new PseudoQueue class. Do not use an existing Queue. Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below), but will internally only utilize 2 Stack objects. Ensure that you create your class with the following methods:
enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.
dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.
The Stack instances have only push, pop, and peek methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.

## Approach & Efficiency
The PseudoQueue can both only be modified by its class methods.  The PseudoQueue is FIFO.  New node elements are added to the rear and removed nodes are pulled from the front.  Given these access methods and structure, all of the methods are Big O(1) for both memory and time.

## API
**The methods available for the Stack class are:**
- *push(value_to_add):*  add the value supplied to the top of the stack to the front
- *pop*:  remove and return the value of the top of the stack
- *is_empty:*  returns true if the stack is empty
- *peek*:  returns the value of the top of the stack
**The methods available for the Queue class are:**
- *enqueue(value_to_add):*  add the value supplied to the rear of the queue
- *dequeue:*  remove and return the value at the front of the queue
- *is_empty:*  returns true if the queue is empty
- *peek*:  returns the value at the front of the queue

## Solution
[Picture of Whiteboard Exercise](code_challenges/Code_Challenge_11.png)

-----------------------------------------------------------------

# Stacks and Queues (Code Challenge 10)
Create a package defining classes for Nodes, Stacks, and Queues to provide a structure for data.

## Challenge
Create a Stack class definition that can be used to create an instance of a stack data structure.  It will be composed of nodes and has the methods of push, pop, is_empty, and peek.  It has an attribute of top.  Create a Queue class definition that can be used to create an instance of a queue data structure.  It will be composed of nodes and has the methods of enqueue, dequeue, is_empty, and peek.  It has attritubes of rear and front.

## Approach & Efficiency
The stack and queue can both only be modified by their class methods.  The stack is FILO and can only be accessed by its head.  The queue is FIFO and has pointers of front and rear.  New node elements are added to the rear and removed nodes are pulled from the front.  Given these access methods and structure, all of the methods for both of these classes are Big O(1) for both memory and time.

## API
**The methods available for the Stack class are:**
- *push(value_to_add):*  add the value supplied to the top of the stack to the front
- *pop*:  remove and return the value of the top of the stack
- *is_empty:*  returns true if the stack is empty
- *peek*:  returns the value of the top of the stack
**The methods available for the Queue class are:**
- *enqueue(value_to_add):*  add the value supplied to the rear of the queue
- *dequeue:*  remove and return the value at the front of the queue
- *is_empty:*  returns true if the queue is empty
- *peek*:  returns the value at the front of the queue


-----------------------------------------------------------------


# Linked List: Zip Two Linked Lists  (Code Challenge 8)
Create a function to zip two linked lists together.

## Challenge
Create a function, when given two linked lists, zips the two linked lists together in a way that alternates between each list.  The function should be able to handle linked lists of different lengths, regardless of order provided as arguments.

## Approach & Efficiency
Progression through both linked lists occurs using a common while loop while two unique "current" position trackers pace through their respective linked lists.  Two temporary variables are used to retain the next_node location as next_node attributes are overwritten.  The time related Big O for this operation is O(n).  For the most part, the memory is Big O(1).  However, if the linked list node's themselves contain a large amount of data, when that data is stored in the temporary value... it could still have a Big O(n) impact?  After some discussion in class, we learned that Big O is large scale and broad strokes.  Therefore, it is more of the size of the input list that makes it O(n), not the size of an individual element or node.  Therefore, this approach is Big O(1).

## Solution
[Picture of Whiteboard Exercise](code_challenges/linked_list/CodeChallenge8.png)



-----------------------------------------------------------------


# Linked List: K-th Value From the End  (Code Challenge 7)
Add one new method to the Linked List class defined during Challenge 5.  This method will find the value a certain number of positions from the end.

## Challenge
Create the following methods to insert new nodes into a Linked List:
1. kthFromEnd: For a given integer, find the value stored in the node that is that number of positions ahead of the end of the Linked List.
1. Stetch: middleValue: Find the number in the center position of a Linked List

## Approach & Efficiency
While loops are used to step two "node tracking variables" through the linked list nodes.  One node recieves a headstart and searches for the end of the list.  The head start is provided by a conditional statement to delay the second "node tracking variable".  If statement conditionals are also used to identify edge and error cases.  In regards to Big O, the time required for the approach is linear, O(n).  That is because we may have to go to the last node in the Linked List.  Memory is only being used to store a single value result (constant), so therefore it is O(1).  HOWEVER... if the value stored in that node is a more data intense value (like another list), it may become a Big O(n).

## Solution
[Picture of Whiteboard Exercise](code_challenges/linked_list/CodeChallenge7.png)



-----------------------------------------------------------------


# Linked List Insertions  (Code Challenge 6)
Add three new methods of insertion to the Linked List class defined during Challenge 5.

## Challenge
Create the following methods to insert new nodes into a Linked List:
1. append: add a new node to the end of the list
1. insertBefore: insert a new node before the node containing the target value
1. insertAfter: insert a new node after the node containing the target value

## Approach & Efficiency
While loops are used to step through the linked list nodes while using if conditionals to find target values or the end of the Linked List.  The previously defined Node Class is used to instantiate the new node.  In regards to Big O, both the time and memory required for these three approaches are linear, O(n).

## Solution
[Picture of Whiteboard Exercise](code_challenges/linked_list/CodeChallenge6.png)



-----------------------------------------------------------------
# Singly Linked List  (Code Challenge 5)
Created the structure to instantiate a singly linked list through the use of a LinkedList class and Node class.

## Challenge
Create a singly linked list architecture and structure using classes.  Provide methods to create a new linked list, add nodes to it, search if a value is stored in the linked list, and to provide a string version of all of the values.

## Approach & Efficiency
Linked lists provide Big O benefits over the use of arrays when adding new values to the dataset.  This architecture stores any additional values added to the linked list in the head position, providing a Big O(1) for time.  The memory required is still dependent on the input and its size, making it Big O(n).

## API
This module may be interacted with to do several things.  Below is a description of how to instantiate a new list and the methods available on it.

1. Create a new singly Linked List by calling on the class:  your_new_list = LinkedList()
2. Add a value to the class:  your_new_list.insert(value)
3. Determine if a value is in a linked list:  your_new_list.includes(value)
4. Create a string containing all of the values in the list:  your_new_list.__str__



-----------------------------------------------------------------
# Array Binary Search  (Code Challenge 3)
The challenge is to produce a function that finds the index position of a given value within a given array.

## Challenge
Without using built in functions designed for this purpose, code a function to accomplish the same outcome in a verbose way using simple built in functions.

## Approach & Efficiency
My partner, Alex Pena, and I used math, if/else statements, and a recursive subfunction to accomplish the task.  In regards to Big O, both the time and memory required for this approach are logarithmic, O(log n).

## Solution
- [Picture of Whiteboard Exercise #1](code_challenges/array_binary_search/whiteboard-code-3.png)
- [Picture of Whiteboard Exercise #2](code_challenges/array_binary_search/Visual-Code-3.png)
- [Picture of Whiteboard Exercise #3](code_challenges/array_binary_search/Visual-Code-Handle-Not-Found.png)






-----------------------------------------------------------------
# Insert Shift Array  (Code Challenge 2)
The challenge is to produce a function that inserts a new number into the middle of an array.

## Challenge
Without using built in functions to insert a number into an array, code a function to accomplish the same outcome in a verbose way using simple built in functions.

## Approach & Efficiency
My partners, James Swift and Yoni Palagashvili, used math, rounding function, if/else statements, a for loop, and list addition to produce the results.  In regards to Big O, both the time and memory required for this approach are linear, O(n).

## Solution
[Picture of Whiteboard Exercise](code_challenges/array_shift/array_shift.png)




-----------------------------------------------------------------
# Reverse an Array (Code Challenge 1)
The challenge is to produce a function that reverses an array using low level commands and functions.

## Challenge
Without using built in functions to reverse an array, code a function to accomplish the same outcome in a verbose way using simple built in functions.

## Approach & Efficiency
My partner, Will Motchoffo, used an array reassignment, the push function, and a for loop to reverse the array.  In regards to Big O, both the time and memory required for this approach are linear, O(n).  On our whiteboard, we had thought the memory for this approach would be constant, O(1), but now I do not think that is correct.

## Solution
[Picture of Whiteboard Exercise](code_challenges/array_reverse/reverse_array.png)





-----------------------------------------------------------------
-----------------------------------------------------------------


# Standard/Template Info:

### Folder and Challenge Setup

Each type of code challenge has slightly different instructions. Please refer to the notes and examples below for instructions for each DS&A assignment type.

### Data Structure: New Implementation

- Create a new folder under the `python` level, with the name of the data structure and complete your implementation there
  - i.e. `linked_list`
- Implementation (the data structure "class")
  - The implementation of the data structure should match package name
    - i.e. `linked_list/linked_list.py`
  - Follow Python [naming conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

    ```python
    class LinkedList:
      def __init__(self):
        # ... initialization code

      def method_name(self):
        # method body
    ```

- Tests
  - Within folder `tests` create a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Your tests will then need to require the data structure you're testing
      - i.e. `from linked_list.linked_list import LinkedList`

### Data Structure: Extending an implementation

- Work within the existing data structure implementation
- Create a new method within the class that solves the code challenge
  - Remember, you'll have access to `self` within your class methods
- Tests
  - You will have folder named `tests` and within it, a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Add to the tests written for this data structure to cover your new method(s)

### Code Challenge / Algorithm

Code challenges should be completed within a folder named `code_challenges` under the `python` level

- Daily Setup:
  - Create a new folder under the `python` level, with the name of the code challenge
    - Each code challenge assignment identifies the branch name to use, for example 'find-maximum-value'
    - For clarity, create your folder with the same name, ensuring that it's `snake_cased`
    - i.e. For a challenge named 'find_maximum_value', create the folder:`code_challenges/find_maximum_value`
  - Code Challenge Implementation
    - Each code challenge requires a function be written, for example "find maximum value"
    - Name the actual challenge file with the name of the challenge, in `snake_case`
      - i.e. `find_maximum_value.py`
    - Reminder: Your challenge file will then need to require the data structure you're using to implement
      - i.e. `from linked_list.linked_list import LinkedList`
    - Your challenge function name is up to you, but name something sensible that communicates the function's purpose. Obvious is better than clever
      - i.e. `find_maximum_value(linked_list)`
  - Tests
    - Ensure there is a `tests` folder at the root of project.
      - i.e. a sibling of this document.
    - within it, a test file called `test_[challenge].py`
      - i.e. `tests/find_maximum_value.py`
      - Your test file would require the challenge file found in the directory above, which has your exported function
        - i.e. `from code_challenges.find_maximum_value import find_maximum_value`

## Running Tests

If you setup your folders according to the above guidelines, running tests becomes a matter of deciding which tests you want to execute.  Jest does a good job at finding the test files that match what you specify in the test command

From the root of the `data-structures-and-algorithms/python` folder, execute the following commands:

- **Run every possible test** - `pytest`
- **Run filtered tests** - `pytest -k some_filter_text`
- **Run in watch mode** - `ptw` or `pytest-watch`
