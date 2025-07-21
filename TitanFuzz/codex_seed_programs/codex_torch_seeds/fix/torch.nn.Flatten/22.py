'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Flatten\ntorch.nn.Flatten(start_dim=1, end_dim=-1)\n'
import torch
import torch.nn as nn
import torch
x = torch.randn(1, 2, 3, 4)
flatten = nn.Flatten(start_dim=1, end_dim=(- 1))
print(flatten(x))