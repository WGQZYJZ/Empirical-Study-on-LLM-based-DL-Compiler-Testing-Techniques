'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LPPool2d\ntorch.nn.LPPool2d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
from torch import nn
dtype = torch.float
device = torch.device('cpu')
(N, C, H, W) = (1, 4, 5, 5)
x = torch.randn(N, C, H, W, device=device, dtype=dtype)
pool = nn.LPPool2d(2, kernel_size=3, stride=2, ceil_mode=False)
y = pool(x)
print(y)