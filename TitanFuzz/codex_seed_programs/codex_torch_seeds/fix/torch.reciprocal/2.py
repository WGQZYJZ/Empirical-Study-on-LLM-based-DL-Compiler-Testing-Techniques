'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reciprocal\ntorch.reciprocal(input, *, out=None)\n'
import torch
input = torch.randn(2, 3)
print('Input data:', input)
output = torch.reciprocal(input)
print('Output data:', output)