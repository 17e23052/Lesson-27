message = ""
not_done = True
while not_done:
  print("Enter a decimal number to be converted or enter 'done' if you are done:")
  number = input().lower()
  letter = chr(number)
  message = message + letter
  if number == "done":
    not_done = False
print("Message:")
print(message)