'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GELU\ntorch.nn.GELU()\n'
import torch
import torch.nn as nn
x = torch.randn(1, 1, 4, 4)
print(x)
gelu = nn.GELU()
print(gelu(x))