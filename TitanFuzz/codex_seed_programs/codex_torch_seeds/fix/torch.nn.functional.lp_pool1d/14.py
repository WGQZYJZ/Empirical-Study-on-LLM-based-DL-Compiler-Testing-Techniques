'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.lp_pool1d\ntorch.nn.functional.lp_pool1d(input, norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 1, 4, requires_grad=True)
output = nn.functional.lp_pool1d(input, norm_type=2, kernel_size=2)
print(output)
output.backward(torch.ones_like(output))
print(input.grad)