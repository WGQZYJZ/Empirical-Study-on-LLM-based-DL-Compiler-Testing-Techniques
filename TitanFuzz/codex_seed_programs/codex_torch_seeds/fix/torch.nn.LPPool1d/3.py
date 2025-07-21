'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LPPool1d\ntorch.nn.LPPool1d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
from torch.nn import LPPool1d
input = torch.randn(1, 1, 5)
pool = LPPool1d(1, kernel_size=2)
output = pool(input)
print(output)