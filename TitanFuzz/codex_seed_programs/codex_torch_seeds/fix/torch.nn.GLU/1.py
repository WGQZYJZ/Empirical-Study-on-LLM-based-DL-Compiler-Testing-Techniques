'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GLU\ntorch.nn.GLU(dim=-1)\n'
import torch
import torch.nn as nn
print(torch.__version__)
x = torch.randn(3, 4)
print(x)
m = nn.GLU(dim=(- 1))
print(m(x))