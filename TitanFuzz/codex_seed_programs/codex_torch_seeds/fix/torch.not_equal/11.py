'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.not_equal\ntorch.not_equal(input, other, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('Input data: \n', input)
output = torch.not_equal(input, 0)
print('Output data: \n', output)