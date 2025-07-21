'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Mish\ntorch.nn.Mish(inplace=False)\n'
import torch
import torch.nn as nn
import torch
x = torch.randn(100, 100)
mish = nn.Mish()
print(mish(x))
mish = nn.Mish(inplace=False)
print(mish(x))