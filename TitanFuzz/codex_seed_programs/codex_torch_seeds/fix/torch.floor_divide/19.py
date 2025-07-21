'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor_divide\ntorch.floor_divide(input, other, *, out=None)\n'
import torch
input = torch.randint(10, (3, 3), dtype=torch.float)
other = torch.randint(10, (3, 3), dtype=torch.float)
print('Input: ', input)
print('Other: ', other)
print('Floor division: ', torch.floor_divide(input, other))