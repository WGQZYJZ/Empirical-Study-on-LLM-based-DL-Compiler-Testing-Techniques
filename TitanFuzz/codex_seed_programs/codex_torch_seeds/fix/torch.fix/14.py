'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fix\ntorch.fix(input, *, out=None)\n'
import torch
input = torch.randn(4, dtype=torch.float)
print('input:', input)
output = torch.fix(input)
print('output:', output)