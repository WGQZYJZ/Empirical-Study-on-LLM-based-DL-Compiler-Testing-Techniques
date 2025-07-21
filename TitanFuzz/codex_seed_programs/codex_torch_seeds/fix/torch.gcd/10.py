'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gcd\ntorch.gcd(input, other, *, out=None)\n'
import torch
input = torch.randint(low=10, high=100, size=(4,))
other = torch.randint(low=10, high=100, size=(4,))
output = torch.gcd(input, other)
print(output)