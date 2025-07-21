'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool3d\ntorch.nn.functional.max_pool3d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
from torch.nn.functional import max_pool3d
print('PyTorch version:')
print(torch.__version__)
print('Configuration:')
print(torch.__config__.show())
input_data = Variable(torch.randn(1, 1, 2, 3, 3))
print('Input data:')
print(input_data)
pooled = max_pool3d(input_data, kernel_size=2, stride=1, padding=1)
print('Pooled data:')
print(pooled)