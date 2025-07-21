'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool1d\ntorch.nn.functional.max_pool1d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import numpy as np
batch_size = 3
num_channels = 1
sequence_length = 5
input_data = torch.randn(batch_size, num_channels, sequence_length)
output_data = torch.nn.functional.max_pool1d(input_data, kernel_size=2, stride=1, padding=0)
print('input_data: ', input_data)
print('output_data: ', output_data)