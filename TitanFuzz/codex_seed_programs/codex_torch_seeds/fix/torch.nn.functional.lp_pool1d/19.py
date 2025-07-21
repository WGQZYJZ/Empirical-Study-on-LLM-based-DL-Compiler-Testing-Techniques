'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.lp_pool1d\ntorch.nn.functional.lp_pool1d(input, norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
import torch.nn.functional as F
import torch
input = torch.randn(1, 1, 4, requires_grad=True)
output = F.lp_pool1d(input, norm_type=1, kernel_size=2)
print(output)