'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.lp_pool1d\ntorch.nn.functional.lp_pool1d(input, norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
input_data = torch.rand(1, 1, 5)
output_data = torch.nn.functional.lp_pool1d(input_data, norm_type=2, kernel_size=3, stride=2, ceil_mode=False)
print('input_data: ', input_data)
print('output_data: ', output_data)