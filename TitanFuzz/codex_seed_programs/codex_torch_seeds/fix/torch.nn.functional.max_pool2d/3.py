'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool2d\ntorch.nn.functional.max_pool2d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
input = torch.randn(2, 3, 5, 5)
max_pool = F.max_pool2d(input, kernel_size=3, stride=2, padding=1)
print(max_pool.size())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool2d\ntorch.nn.functional.max_pool2d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
input = torch.randn(2, 3, 5, 5)