'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.lp_pool1d\ntorch.nn.functional.lp_pool1d(input, norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
import torch
input_data = torch.randn(1, 1, 4)
print(input_data)
output_data = torch.nn.functional.lp_pool1d(input_data, 1, 2, stride=2)
print(output_data)