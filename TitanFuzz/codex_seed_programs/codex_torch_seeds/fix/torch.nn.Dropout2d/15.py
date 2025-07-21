'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout2d\ntorch.nn.Dropout2d(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
x = torch.randn(1, 10, 10)
out = nn.Dropout2d(p=0.5)(x)
print(out)