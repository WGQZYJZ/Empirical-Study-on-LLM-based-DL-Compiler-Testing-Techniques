'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.not_equal\ntorch.not_equal(input, other, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('Input: \n', input)
other = torch.randn(3, 3)
print('Other: \n', other)
output = torch.not_equal(input, other)
print('Output: \n', output)