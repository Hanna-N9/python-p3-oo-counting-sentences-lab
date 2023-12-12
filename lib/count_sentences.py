#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ""):
    self._value = value
  
  @property  
  def get_value(self):
    return self._value

  @value.setter
  def set_value(self, stringVal):
    if isinstance(value, str):
      self._value = stringVal
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self._value.endswith(".")

  def is_question(self):
    return self._value.endswith("?")

  def is_exclamation(self):
    return self._value.endswith("!")

  def count_sentences(self):
    value = self.value
    for punctuation in ["!","?"]:
        value = value.replace(punctuation, ".")
        
    return len([sentence for sentence in value.split(".") if sentence])
    