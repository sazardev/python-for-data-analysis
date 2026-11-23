strings = ["a", "as", "bat", "car", "dove"]

"""
This is an example and equivalent from:
  result = []
  for value in collection:
    if condition:
      result.append(expr)
"""
print([x.upper() for x in strings if len(x) > 2])
