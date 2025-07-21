'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GLU\ntorch.nn.GLU(dim=-1)\n'
import torch
import torch.nn as nn
x = torch.randn(2, 3, 4)
glu = nn.GLU(dim=(- 1))
print(glu(x))