'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.acos\ntorch.acos(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print('The input is:\n', input)
output = torch.acos(input)
print('The output is:\n', output)