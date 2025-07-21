'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool1d\ntorch.nn.MaxPool1d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(2, 3, 3)
print(input_data)
max_pool = nn.MaxPool1d(kernel_size=2, stride=2)
output_data = max_pool(input_data)
print(output_data)
print(output_data.shape)