'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gcd\ntorch.gcd(input, other, *, out=None)\n'
import torch
input = torch.randint(1, 100, (5, 5), dtype=torch.long)
other = torch.randint(1, 100, (5, 5), dtype=torch.long)
print('input: ', input)
print('other: ', other)
out = torch.gcd(input, other)
print('out: ', out)