'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.fractional_max_pool2d\ntorch.nn.functional.fractional_max_pool2d(*args, **kwargs)\n'
import torch
from torch.autograd import Variable
import torch
input = torch.randn(1, 1, 5, 5)
output = torch.nn.functional.fractional_max_pool2d(input, kernel_size=(3, 3), output_size=(3, 3))
print('Input shape: {}'.format(input.shape))
print('Output shape: {}'.format(output.shape))