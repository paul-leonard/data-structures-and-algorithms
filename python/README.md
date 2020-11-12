# Data Structures and Algorithms

## Language: `Python`


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
