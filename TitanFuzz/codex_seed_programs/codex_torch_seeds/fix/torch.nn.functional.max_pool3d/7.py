'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool3d\ntorch.nn.functional.max_pool3d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
input_data = torch.randn(1, 1, 5, 5, 5)
print('Input data: \n{}'.format(input_data))
output_data = torch.nn.functional.max_pool3d(input_data, kernel_size=3, stride=1, padding=1)
print('Output data: \n{}'.format(output_data))