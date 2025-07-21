'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gcd\ntorch.gcd(input, other, *, out=None)\n'
import torch
input = torch.randint(low=0, high=100, size=(1,), dtype=torch.int)
other = torch.randint(low=0, high=100, size=(1,), dtype=torch.int)
print(input)
print(other)
print(torch.gcd(input, other))