'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.conv1d\ntorch.nn.functional.conv1d(input, weight, bias=None, stride=1, padding=0, dilation=1, groups=1)\n'
import torch
import numpy as np
import torch
input_data = torch.randn(1, 1, 4)
print('Input data: ', input_data)
weight_data = torch.randn(1, 1, 3)
print('Weight data: ', weight_data)
output = torch.nn.functional.conv1d(input_data, weight_data)
print('Output: ', output)