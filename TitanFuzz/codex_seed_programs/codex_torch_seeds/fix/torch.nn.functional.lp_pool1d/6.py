'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.lp_pool1d\ntorch.nn.functional.lp_pool1d(input, norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
input_data = torch.randn(1, 1, 5)
print(f'Input data: {input_data}')
output_data = torch.nn.functional.lp_pool1d(input_data, 1, 3, stride=1, ceil_mode=False)
print(f'Output data with norm_type = 1: {output_data}')
output_data = torch.nn.functional.lp_pool1d(input_data, 2, 3, stride=1, ceil_mode=False)
print(f'Output data with norm_type = 2: {output_data}')
output_data = torch.nn.functional.lp_pool1d(input_data, float('inf'), 3, stride=1, ceil_mode=False)