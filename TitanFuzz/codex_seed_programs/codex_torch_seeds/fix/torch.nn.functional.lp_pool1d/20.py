'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.lp_pool1d\ntorch.nn.functional.lp_pool1d(input, norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 1, 5)
print(input)
output = F.lp_pool1d(input, norm_type=2, kernel_size=3, stride=2, ceil_mode=False)
print(output)
output = F.lp_pool1d(input, norm_type=2, kernel_size=3, stride=2, ceil_mode=True)
print(output)