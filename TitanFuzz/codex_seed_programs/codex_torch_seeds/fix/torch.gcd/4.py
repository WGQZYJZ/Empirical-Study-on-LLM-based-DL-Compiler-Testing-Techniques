'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gcd\ntorch.gcd(input, other, *, out=None)\n'
import torch
a = torch.randint(1, 10, (3, 3))
b = torch.randint(1, 10, (3, 3))
print('a = ', a)
print('b = ', b)
print('GCD of a and b = ', torch.gcd(a, b))