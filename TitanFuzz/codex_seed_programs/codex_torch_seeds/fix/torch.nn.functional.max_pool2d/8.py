'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool2d\ntorch.nn.functional.max_pool2d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 1, 3, 3)
output = F.max_pool2d(input, kernel_size=2, stride=2)
print(output)