'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FractionalMaxPool2d\ntorch.nn.FractionalMaxPool2d(kernel_size, output_size=None, output_ratio=None, return_indices=False, _random_samples=None)\n'
import torch
import torch.nn as nn
import numpy as np
input = torch.randn(1, 1, 8, 8)
print('Input Data:')
print(input)
fractional_max_pooling = nn.FractionalMaxPool2d(3, output_size=(3, 3))
output = fractional_max_pooling(input)
print('Output Data:')
print(output)