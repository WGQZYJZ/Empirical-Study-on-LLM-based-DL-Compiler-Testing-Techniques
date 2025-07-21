'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gcd\ntorch.gcd(input, other, *, out=None)\n'
import torch
input = torch.randint(low=1, high=10, size=(3, 3), dtype=torch.int32)
other = torch.randint(low=1, high=10, size=(3, 3), dtype=torch.int32)
print('Input: ', input)
print('Other: ', other)
print('Result: ', torch.gcd(input, other))