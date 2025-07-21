'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool1d\ntorch.nn.functional.adaptive_max_pool1d(input, output_size, return_indices=False)\n'
import torch
from torch.nn.functional import adaptive_max_pool1d
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_data = torch.arange(1, 11, dtype=torch.float32).view(1, 1, 10)
print('Input data: ', input_data)
print('Task 3: Call the API torch.nn.functional.adaptive_max_pool1d')
output_size = 3
output_data = adaptive_max_pool1d(input_data, output_size)
print('output_data: ', output_data)