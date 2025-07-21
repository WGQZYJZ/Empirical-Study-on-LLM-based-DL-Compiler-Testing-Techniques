'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.div\ntorch.div(input, other, *, rounding_mode=None, out=None)\n'
import torch
input = torch.randn(5, 5)
other = torch.randn(5, 5)
output = torch.div(input, other)
print('input: ', input)
print('other: ', other)
print('output: ', output)