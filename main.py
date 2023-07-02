# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def password_modifier(password):
  """Modifies a password by replacing certain characters and appending "q*s" to the end.

  Args:
    password: The password to be modified.

  Returns:
    The modified password.
  """

  modified_password = ""
  for char in password:
    if char == "i":
      modified_password += "!"
    elif char == "a":
      modified_password += "@"
    elif char == "m":
      modified_password += "M"
    elif char == "B":
      modified_password += "8"
    elif char == "o":
      modified_password += "."
    else:
      modified_password += char

  modified_password += "q*s"
  return modified_password


def main():
  """Prompts the user for a password and then prints the modified password."""

  
  modified_password = password_modifier(password)
  print({modified_password})


if __name__ == "__main__":
  main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
