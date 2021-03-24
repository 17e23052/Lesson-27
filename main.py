message = ""
not_done = True
while not_done:
  print("Enter a decimal number to be converted or enter '00' if you are done:")
  number = int(input())
  letter = chr(number)
  message = message + letter
  if number == 00:
    not_done = False
print()
print("Message:")
print(message)