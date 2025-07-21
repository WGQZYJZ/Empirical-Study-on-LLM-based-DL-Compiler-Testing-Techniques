'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.fractional_max_pool2d\ntorch.nn.functional.fractional_max_pool2d(*args, **kwargs)\n'
import torch
from torch.nn.functional import fractional_max_pool2d
import torch.nn as nn
import torch.nn.functional as F
input = torch.randn(1, 1, 32, 32)
output = fractional_max_pool2d(input, kernel_size=[2, 2], output_size=[2, 2], output_ratio=[0.5, 0.5])
print('output: ', output)