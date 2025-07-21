'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gcd\ntorch.gcd(input, other, *, out=None)\n'
import torch
input = torch.randint(1, 20, (5,), dtype=torch.int32)
other = torch.randint(1, 20, (5,), dtype=torch.int32)
print('Input data:')
print(input)
print(other)
print('Output data:')
print(torch.gcd(input, other))