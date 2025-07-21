'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Linear\ntorch.nn.Linear(in_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
x = torch.randn(1, 3)
linear = nn.Linear(in_features=3, out_features=2)
print(linear(x))