'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.lp_pool2d\ntorch.nn.functional.lp_pool2d(input, norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
input = torch.randn(20, 16, 50, 32)
output = torch.nn.functional.lp_pool2d(input, 2, (2, 2))
print(output.size())