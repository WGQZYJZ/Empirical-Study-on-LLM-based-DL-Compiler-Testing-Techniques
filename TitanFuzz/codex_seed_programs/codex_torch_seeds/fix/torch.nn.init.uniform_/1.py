'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.uniform_\ntorch.nn.init.uniform_(tensor, a=0.0, b=1.0)\n'
import torch
import torch.nn as nn
x = torch.rand(3, 4)
nn.init.uniform_(x, 0, 1)
print(x)