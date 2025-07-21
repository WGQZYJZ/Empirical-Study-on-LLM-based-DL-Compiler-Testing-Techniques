'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FractionalMaxPool3d\ntorch.nn.FractionalMaxPool3d(kernel_size, output_size=None, output_ratio=None, return_indices=False, _random_samples=None)\n'
import torch
from torch.nn.modules.module import Module
from torch.nn.parameter import Parameter
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data
import torch
input = torch.randn(20, 16, 50, 32, 32)
pool = nn.FractionalMaxPool3d(3, output_size=(5, 5, 5))
output = pool(input)
print(output.size())