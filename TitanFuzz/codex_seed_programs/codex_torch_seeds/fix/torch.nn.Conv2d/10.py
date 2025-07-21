"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Conv2d\ntorch.nn.Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True, padding_mode='zeros', device=None, dtype=None)\n"
import torch
import torch.nn as nn
import numpy as np
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_data = np.random.rand(1, 1, 5, 5)
input_data = torch.from_numpy(input_data).float()
print('Task 3: Call the API torch.nn.Conv2d')
conv2d = nn.Conv2d(in_channels=1, out_channels=1, kernel_size=3)
output_data = conv2d(input_data)
print('Input shape: ', input_data.shape)
print('Output shape: ', output_data.shape)