'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LPPool1d\ntorch.nn.LPPool1d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(2, 3, 5)
print(input)
pool = nn.LPPool1d(2, 3, stride=2)
output = pool(input)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LPPool2d\ntorch.nn.LPPool2d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch