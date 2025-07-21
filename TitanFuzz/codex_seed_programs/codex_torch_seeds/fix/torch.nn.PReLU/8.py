'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PReLU\ntorch.nn.PReLU(num_parameters=1, init=0.25, device=None, dtype=None)\n'
import torch
import torch.nn as nn
x = torch.randn(2, 2)
prelu = nn.PReLU(num_parameters=1, init=0.25)
print(prelu(x))