'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eq\ntorch.eq(input, other, *, out=None)\n'
import torch
input = torch.randn(3, 3)
other = torch.randn(3, 3)
output = torch.eq(input, other)
print('input: ', input)
print('other: ', other)
print('output: ', output)