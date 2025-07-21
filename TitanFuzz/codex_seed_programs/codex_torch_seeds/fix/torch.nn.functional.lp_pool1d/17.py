'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.lp_pool1d\ntorch.nn.functional.lp_pool1d(input, norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 1, 8)
output = F.lp_pool1d(input, 2, 3, 1)
print(output)