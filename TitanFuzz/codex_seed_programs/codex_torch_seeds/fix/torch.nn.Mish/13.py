'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Mish\ntorch.nn.Mish(inplace=False)\n'
import torch
import torch.nn as nn
x = torch.randn(1, 3, 3, 3)
mish = nn.Mish(inplace=False)
y = mish(x)
print(y)