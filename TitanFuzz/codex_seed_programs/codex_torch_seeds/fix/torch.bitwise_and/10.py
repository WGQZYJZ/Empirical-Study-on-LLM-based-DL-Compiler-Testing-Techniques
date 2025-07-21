'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_and\ntorch.bitwise_and(input, other, *, out=None)\n'
import torch
input = torch.randint(0, 2, (4,), dtype=torch.bool)
other = torch.randint(0, 2, (4,), dtype=torch.bool)
print('Input:', input)
print('Other:', other)
output = torch.bitwise_and(input, other)
print('Output:', output)