#Number 1
def string_length(text):
  """Calculates the length of a string without using len().

  Args:
      text: The string to analyze.

  Returns:
      The length (number of characters) of the string.
  """
  count = 0
  for char in text:
    count += 1
  return count

# Get user input
User = input("Enter a string: ")

# Call the function to calculate length
string_len = string_length(User)

# Print the result
print(f"The length of the string '{User}' is: {string_len}")

#Number 2

def char_frequency(text):
  """Counts the frequency of each character in a string.

  Args:
      text: The string to analyze.

  Returns:
      A dictionary where keys are characters and values are their frequencies.
  """
  char_counts = {}
  for char in text:
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1
  return char_counts

# Get user input
Y = input("Enter a string: ")

# Call the function to count character frequencies
char_freq = char_frequency(Y)

# Print the results
print("Character frequencies:")
for char, count in char_freq.items():
  print(f"\t- {char}: {count}")
  
  
#Number 4
def concatenate_and_swap(str1, str2):
  """Concatenates two strings and swaps their first two characters.

  Args:
      str1: The first string.
      str2: The second string.

  Returns:
      A tuple containing the concatenated string with swapped characters and the swapped characters.
  """
  swapped_chars = str1[:2] + str2[:2]
  concatenated_str = str2[2:] + str1[2:]
  return concatenated_str, swapped_chars

# Get user input
Str1 = input("Enter the first string: ")
Str2 = input("Enter the second string: ")

# Call the function to concatenate and swap characters
concatenated_string, swapped_chars = concatenate_and_swap(Str1, Str2)

# Print the results
print(f"Concatenated string with swapped characters: {concatenated_string}")
print(f"Swapped characters: {swapped_chars}")

#number 7
def remove_odd_indices(text):
  """Removes characters at odd indices from a string.

  Args:
      text: The string to modify.

  Returns:
      A new string with characters at odd indices removed.
  """
  new_string = ""
  for i, char in enumerate(text):
    # Include only characters at even indices (i % 2 == 0)
    if i % 2 == 0:
      new_string += char
  return new_string

# Get user input
Odd = input("Enter a string: ")

# Call the function to remove characters at odd indices
ResultString = remove_odd_indices(Odd)

# Print the result
print(f"Modified String: {ResultString}")


#Number 10
def reverse_string(text):
  """Reverses a string using slicing and concatenation.

  Args:
      text: The string to be reversed.

  Returns:
      The reversed string.
  """
  reversed_text = ""
  for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]
  return reversed_text

# Get user input
ReverseChr = input("Enter a string: ")

# Call the function to reverse the string
reversed_string = reverse_string(ReverseChr)

# Print the result
print(f"Reversed string: {reversed_string}")


#Number 12
def reverse_words(text):
  """Reverses the order of words in a string.

  Args:
      text: The string with words to be reversed.

  Returns:
      A new string with the words reversed.
  """
  # Split the string into words
  words = text.split()

  # Reverse the list of words
  reversed_words = words[::-1]

  # Join the reversed words back into a string
  return " ".join(reversed_words)

# Get user input
Word = input("Enter a string: ")

# Call the function to reverse words
ReversedWord = reverse_words(Word)

# Print the result
print(f"String with reversed words: {ReversedWord}")

#Number 16
def sum_of_digits(text):
  """Calculates the sum of digits in a string.

  Args:
      text: The string to analyze.

  Returns:
      The sum of digits in the string (or 0 if no digits are found).
  """
  total_sum = 0
  for char in text:
    # Check if character is a digit (0-9) using isdigit()
    if char.isdigit():
      # Convert the digit character to an integer and add to the sum
      total_sum += int(char)
  return total_sum

# Get user input
Value1 = input("Enter a string: ")

# Call the function to calculate the sum of digits
digit_sum = sum_of_digits(Value1)

# Print the result with a check for no digits
if digit_sum > 0:
  print(f"Sum of digits in '{Value1}': {digit_sum}")
else:
  print(f"The string '{Value1}' does not contain any digits.")
  
#Number 18
def count_char_types(text):
  """Counts the occurrences of uppercase letters, lowercase letters, digits, and special characters in a string.

  Args:
      text: The string to analyze.

  Returns:
      A dictionary containing counts for uppercase, lowercase, digits, and special characters.
  """
  char_counts = {
      "uppercase": 0,
      "lowercase": 0,
      "digits": 0,
      "special": 0,
  }
  for char in text:
    if char.isupper():
      char_counts["uppercase"] += 1
    elif char.islower():
      char_counts["lowercase"] += 1
    elif char.isdigit():
      char_counts["digits"] += 1
    else:
      char_counts["special"] += 1
  return char_counts

# Get user input
Character = input("Enter a string: ")

# Call the function to count character types
char_type_counts = count_char_types(Character)

# Print the results in a clear format
print("Character counts:")
for char_type, count in char_type_counts.items():
  print(f"\t- {char_type}: {count}")
  
  
#Number 31
def generate_permutations(text):
  """Generates all permutations of a string using recursion.

  Args:
      text: The string for which to generate permutations.

  Yields:
      Each permutation of the string as a string.
  """
  if len(text) == 1:
    yield text
  else:
    for i in range(len(text)):
      first = text[i]
      rest = text[:i] + text[i + 1:]
      # Recursively generate permutations of the remaining characters
      for perm in generate_permutations(rest):
        yield first + perm

# Get user input
Value = input("Enter a string: ")

# Generate all permutations
print("All permutations:")
for permutation in generate_permutations(Value):
  print(permutation)

#Number 22
def delete_all_occurrences(text, char):
  """Deletes all occurrences of a specified character from a string.

  Args:
      text: The string to modify.
      char: The character to remove.
  """
  new_string = ""
  for char_in_text in text:
    if char_in_text != char:
      new_string += char_in_text
  # No return statement needed, modification happens in-place

# Get user input
word = input("Enter a string: ")
removeValue = input("Enter the Letter to remove: ")

# Call the function to remove characters
delete_all_occurrences(word, removeValue)

# Print the result (modification happens within the function)
print(f"String with '{removeValue}' Letter removed: {word}")












