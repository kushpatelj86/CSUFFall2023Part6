# --------------------WRITE YOUR CODE BELOW-------------------#
import os
import re
import math
import random
import statistics
from datetime import datetime
import timeit
import reprlib
import pprint
import textwrap
import logging
from string import Template
import heapq
def list_files_in_directory(strng="."):
   
   for i in os.listdir(strng):
    if os.path.isfile(os.path.join(strng, i)):
        print(i)

def extract_emails(strng=""):  
    email_adresses = re.findall('\S+@\S+',strng)
    print(email_adresses)

def calculate_square_root(num=4):
    sqrroot = math.sqrt(num)
    print(f"Square Root of {num} is {sqrroot}" )

def generate_random_integer(num1, num2):
    rnd = random.randint(num1,num2)
    print(f"Random Number between {num1} and {num2}: {rnd}")

def calculate_mean_and_stddev(nums=[1,2,3,4]):
    mean = statistics.mean(nums)
    standdevi = statistics.stdev(nums)
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {standdevi}")

def print_current_datetime():
    right_now = datetime.now()
    print("Current Date and Time: ",right_now)

def time_function_execution():
    timeittakes = timeit.Timer("2 + 5 * 3 / 2 ** 6").timeit()
    print("Time taken to execute the function: ",timeittakes )

def truncate_long_string(strng=""):
    trucated_stirng = reprlib.repr(strng)
    print("Truncated String: ", trucated_stirng)

def pretty_print_nested_dict(dct = {'name': 'John', 'age': 30, 'city': 'New York'}):
    pprint.pprint(dct)

def wrap_text_paragraph(para, line_width):
    wrapped = textwrap.wrap(para, line_width)
    for i in wrapped:
        print(i)

def generate_sql_query(sample_table_name, sample_columns):
    t = Template('Generated SQL Query: $sample_columns FROM $sample_table_name') 
    x = t.substitute(sample_table_name =sample_table_name, sample_columns = sample_columns )
    print(x)

def setup_logging():
    logging.debug('Debugging things')
    logging.info('Information message')
    logging.warning('Warning:config file %s not found', 'server.conf')
    logging.error('Error occurred')
    logging.critical('Critical error occured')

def perform_heap_operations(numbers):
    heapq.heapify(numbers)
    print(f"Heapified List: {numbers}")
    min_value = heapq.heappop(numbers)
    print(f"Minimum value: {min_value}")


# --------------------END OF YOUR CODE------------------------#

'''
CREATE THE BELOW CALLED FUNCTION DEFINITION IN YOUR CODE!
'''

if __name__ == '__main__':

    # Sample data for tasks
    sample_text = "Sample email addresses: abc@example.com, xyz@domain.com"
    sample_numbers = [2, 4, 6, 8, 10]
    sample_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
    sample_paragraph = "This is a long paragraph that needs to be wrapped to multiple lines for better readability."
    sample_number = 12345.67
    sample_table_name = "users"
    sample_columns = "id, name, email"
    sample_numbers_for_heap = [3, 1, 4, 1, 5, 9]

    # Task executions
    list_files_in_directory(".")  # Task 1
    extract_emails(sample_text)  # Task 2
    calculate_square_root(16)  # Task 3
    generate_random_integer(1, 100)  # Task 4
    calculate_mean_and_stddev(sample_numbers)  # Task 5
    print_current_datetime()  # Task 6
    time_function_execution()  # Task 7
    truncate_long_string("This is a very long string that needs to be truncated.")  # Task 8
    pretty_print_nested_dict(sample_dict)  # Task 9
    wrap_text_paragraph(sample_paragraph, 30)  # Task 10
    generate_sql_query(sample_table_name, sample_columns)  # Task 11
    setup_logging()  # Task 12
    perform_heap_operations(sample_numbers_for_heap)  # Task 13
