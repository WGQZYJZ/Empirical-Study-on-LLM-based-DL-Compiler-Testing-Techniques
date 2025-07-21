'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.lp_pool2d\ntorch.nn.functional.lp_pool2d(input, norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
import torch.nn.functional as F
import numpy as np
input = torch.randn(1, 1, 4, 4)
output = F.lp_pool2d(input, norm_type=2, kernel_size=2, stride=2)
print(input)
print(output)