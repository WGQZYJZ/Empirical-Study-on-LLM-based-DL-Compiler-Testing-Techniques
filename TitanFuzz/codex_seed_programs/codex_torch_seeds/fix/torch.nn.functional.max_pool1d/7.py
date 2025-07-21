'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool1d\ntorch.nn.functional.max_pool1d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
input_data = torch.randn(1, 1, 4)
print('Input data: ', input_data)
output_data = torch.nn.functional.max_pool1d(input_data, kernel_size=2, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)
print('Output data: ', output_data)
output_data = torch.nn.functional.max_pool1d(input_data, kernel_size=2, stride=2, padding=0, dilation=1, return_indices=False, ceil_mode=False)
print('Output data: ', output_data)