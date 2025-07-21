'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.div\ntorch.div(input, other, *, rounding_mode=None, out=None)\n'
import torch
input = torch.randn(4, 4)
other = torch.randn(4, 4)
output = torch.div(input, other)
print('Input: ', input)
print('Other: ', other)
print('Output: ', output)