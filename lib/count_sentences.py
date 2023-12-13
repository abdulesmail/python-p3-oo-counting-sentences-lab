#!/usr/bin/env python3

class MyString:
   def __init__(self, value=None):
        self._value = None
        if value is not None:
            self.value = value

        @property
        def value(self):
         return self._value

        @value.setter
        def value(self, new_value):
         if not isinstance(new_value, str):
            raise ValueError("The value must be a string.")
        self._value = value

        def is_sentence(self):
         if self._value and self._value.endswith('.'):
            return True
         else:
            return False

        def is_question(self):
         if self._value and self._value.endswith('?'):
            return True
         else:
            return False

        def is_exclamation(self):
         if self._value and self._value.endswith('!'):
            return True
         else:
            return False

        def count_sentences(self):
         if not isinstance(self._value, str):
            raise ValueError("The value must be a string.")

        sentence_count = 0

        for char in self._value:
            if char in ['.', '?', '!']:
                sentence_count += 1

        return sentence_count
   
pass

# Correct Example Usage:
my_string_instance = MyString(value="This is a string! It has three sentences. Right?")

# Access properties as methods, not as iterables
print(my_string_instance.is_sentence())  # Output: False
print(my_string_instance.is_question())  # Output: True
print(my_string_instance.is_exclamation())  # Output: True

# Access the value property directly
print(my_string_instance.value)  # Output: This is a string! It has three sentences. Right?

# Use the count_sentences() method
print(my_string_instance.count_sentences())  # Output: 3




