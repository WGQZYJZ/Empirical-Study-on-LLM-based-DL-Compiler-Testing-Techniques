'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Unflatten\ntorch.nn.Unflatten(dim, unflattened_size)\n'
import torch
import torch.nn as nn
unflattened = nn.Unflatten(dim=1, unflattened_size=(2, 3))
print(unflattened(torch.randn(4, 6)))