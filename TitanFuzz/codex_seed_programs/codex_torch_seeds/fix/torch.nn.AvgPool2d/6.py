'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool2d\ntorch.nn.AvgPool2d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
import numpy as np
from torch.nn import AvgPool2d
input_data = torch.Tensor(np.random.random((1, 1, 4, 4)))
print('Input data: ', input_data)
avg_pool2d = AvgPool2d(kernel_size=2, stride=2)
output = avg_pool2d(input_data)
print('Output: ', output)