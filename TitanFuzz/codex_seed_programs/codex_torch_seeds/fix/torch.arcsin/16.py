'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsin\ntorch.arcsin(input, *, out=None)\n'
import torch
input = torch.randn(2, 3)
print('Input = ', input)
output = torch.arcsin(input)
print('Output = ', output)