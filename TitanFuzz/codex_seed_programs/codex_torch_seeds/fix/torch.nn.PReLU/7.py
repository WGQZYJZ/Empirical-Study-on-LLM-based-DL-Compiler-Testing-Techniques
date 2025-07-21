'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PReLU\ntorch.nn.PReLU(num_parameters=1, init=0.25, device=None, dtype=None)\n'
import torch
from torch.nn import PReLU
x = torch.randn(3, 3)
print(x)
prelu = PReLU(num_parameters=1, init=0.25)
print(prelu(x))