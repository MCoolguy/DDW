def get_permutations(s):
  permutations = []
  stack = [("", s)]
  
  while stack:
    base, chars = stack.pop()
    if not chars:
      permutations.append(base)
    else:
      for i in range(len(chars)):
        stack.append((base + chars[i], chars[:i] + chars[i+1:]))
  
  return permutations

# Example usage
if __name__ == "__main__":
  s = "abc"
  print(get_permutations(s))