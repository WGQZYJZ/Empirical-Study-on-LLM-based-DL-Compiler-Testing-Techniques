'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool3d\ntorch.nn.functional.adaptive_max_pool3d(input, output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch
input = torch.randn(1, 1, 5, 5, 5)
output_size = (3, 3, 3)
output = torch.nn.functional.adaptive_max_pool3d(input, output_size)
print('input size: ', input.size())
print('input: ', input)
print('output size: ', output.size())
print('output: ', output)