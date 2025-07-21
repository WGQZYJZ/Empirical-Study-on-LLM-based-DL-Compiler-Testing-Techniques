'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyLinear\ntorch.nn.LazyLinear(out_features, bias=True, device=None, dtype=None)\n'
import torch
from torch.nn import LazyLinear
x = torch.randn(10, 3)
linear = LazyLinear(3, 5, dtype=torch.float32)
y = linear(x)
print(y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Linear\ntorch.nn.Linear(in_features, out_features, bias=True)\n'
import torch
from torch.nn import Linear
x = torch.randn(10, 3)
linear = Linear(3, 5)
y = linear(x)
print(y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.RReLU\ntorch.nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)\n'
import torch
from torch.nn import RReLU