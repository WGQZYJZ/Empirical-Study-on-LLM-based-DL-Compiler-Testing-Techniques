'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool2d\ntorch.nn.AdaptiveMaxPool2d(output_size, return_indices=False)\n'
import torch
from torch.nn.modules.module import Module
from torch.nn.parameter import Parameter
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
input = torch.randn(1, 1, 5, 5)
print('input: ', input)
output_size = (3, 3)
adaptive_max_pool2d = nn.AdaptiveMaxPool2d(output_size, return_indices=True)