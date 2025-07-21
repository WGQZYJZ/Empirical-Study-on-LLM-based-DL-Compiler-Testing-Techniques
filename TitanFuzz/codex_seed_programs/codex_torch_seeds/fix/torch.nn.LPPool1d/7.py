'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LPPool1d\ntorch.nn.LPPool1d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 1, 5)
print('Input data: ', input_data)
lp_pool1d = nn.LPPool1d(norm_type=2, kernel_size=2)
output_data = lp_pool1d(input_data)
print('Output data: ', output_data)