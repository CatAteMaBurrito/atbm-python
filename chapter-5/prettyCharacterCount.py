import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# Pretty printing
# pprint.pprint(count)

## Similar pretty print function that returns a string instead of printing
print(pprint.pformat(count))