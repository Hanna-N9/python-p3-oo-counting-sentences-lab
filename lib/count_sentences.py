#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
      self.value = value

    @property
    def get_value(self):
      return self._value
  
    @value.setter
    def set_value(self, stringVal):
      if isinstance(value, str):
        self._value = value
      else:
        print("The value must be a string.")
        
    def is_sentence(self):
      return True if self._value.endswith(".") else False
  
    def is_question(self):
      return True self._value.endswith("?") else False
    
    def is_exclamation(self):
      return True self._value.endswith("!") else False
    
    def count_sentences(self):
      value = self.value
      for punctuation in ["!","?"]:
        value = value.replace(punctuation, ".")
      else:
        return len([sentence for sentence in value.split(".") if sentence])