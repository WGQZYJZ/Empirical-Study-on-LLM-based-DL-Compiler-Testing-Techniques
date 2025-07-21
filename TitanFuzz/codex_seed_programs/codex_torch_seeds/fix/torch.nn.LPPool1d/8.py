'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LPPool1d\ntorch.nn.LPPool1d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
data = torch.randn(2, 3, 5)
print('Input data: ', data)
pool = torch.nn.LPPool1d(norm_type=2, kernel_size=3, stride=None, ceil_mode=False)
pool_output = pool(data)
print('Output: ', pool_output)