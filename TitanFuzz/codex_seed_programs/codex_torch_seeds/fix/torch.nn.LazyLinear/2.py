'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyLinear\ntorch.nn.LazyLinear(out_features, bias=True, device=None, dtype=None)\n'
import torch
from torch.nn import LazyLinear
x = torch.randn(1, 10)
linear = LazyLinear(10, 10)
print(linear(x))