s=input()
print(any(w.isalnum() for w in s))
print(any(w.isalpha() for w in s))
print(any(w.isdigit() for w in s))
print(any(w.islower() for w in s))
print(any(w.isupper() for w in s))
