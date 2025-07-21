'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxPool2d\ntorch.nn.MaxPool2d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
input_data = torch.randn(1, 1, 7, 7)
print('Input data: \n', input_data)
max_pool_2d = torch.nn.MaxPool2d(kernel_size=2, stride=2)
output_data = max_pool_2d(input_data)
print('Output data: \n', output_data)