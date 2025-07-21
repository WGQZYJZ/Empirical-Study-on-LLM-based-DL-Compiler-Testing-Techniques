'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.greater\ntorch.greater(input, other, *, out=None)\n'
import torch
input = torch.randn(3, 3)
other = torch.randn(3, 3)
print('Input: \n', input)
print('Other: \n', other)
print('Torch.greater: \n', torch.greater(input, other))