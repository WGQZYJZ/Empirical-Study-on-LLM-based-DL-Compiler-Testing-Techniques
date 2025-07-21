'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gcd\ntorch.gcd(input, other, *, out=None)\n'
import torch
input = torch.randint(0, 1000, (5,))
other = torch.randint(0, 1000, (5,))
output = torch.gcd(input, other)
print('input:', input)
print('other:', other)
print('output:', output)