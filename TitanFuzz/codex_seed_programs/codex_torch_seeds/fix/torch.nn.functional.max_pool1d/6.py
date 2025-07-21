'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool1d\ntorch.nn.functional.max_pool1d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import torch
input_data = torch.randn(1, 1, 3)
max_pool_output = torch.nn.functional.max_pool1d(input_data, 2)
print(input_data)
print(max_pool_output)