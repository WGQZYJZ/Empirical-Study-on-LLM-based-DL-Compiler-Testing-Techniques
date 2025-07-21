'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardsigmoid\ntorch.nn.Hardsigmoid(inplace=False)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(3, 5)
hardsigmoid = nn.Hardsigmoid()
print(hardsigmoid(input))