'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.greater\ntorch.greater(input, other, *, out=None)\n'
import torch
input = torch.randn(2, 2)
print('Input data: ', input)
other = torch.randn(2, 2)
print('Other data: ', other)
result = torch.greater(input, other)
print('Result: ', result)