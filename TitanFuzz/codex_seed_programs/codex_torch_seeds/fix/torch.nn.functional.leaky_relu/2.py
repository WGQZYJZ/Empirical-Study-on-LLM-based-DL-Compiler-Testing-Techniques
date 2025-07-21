'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu\ntorch.nn.functional.leaky_relu(input, negative_slope=0.01, inplace=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
x = torch.randn(3, 3)
F.leaky_relu(x, negative_slope=0.01)
F.leaky_relu(x, negative_slope=0.01, inplace=True)
F.leaky_relu(x, negative_slope=0.01, inplace=False)
y = x.clone()
F.leaky_relu(x, negative_slope=0.01, inplace=True)
(x == y)
x = torch.randn(3, 3)
y = torch.randn(3, 3)
F.leaky_relu(x, negative_slope=0.01, inplace=True)