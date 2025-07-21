'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyLinear\ntorch.nn.LazyLinear(out_features, bias=True, device=None, dtype=None)\n'
import torch
import numpy as np
x = torch.randn(10, 3)
print(x)
lazy_linear = torch.nn.LazyLinear(3, 4)
print(lazy_linear)
y = lazy_linear(x)
print(y)
weight = lazy_linear.weight
print(weight)
bias = lazy_linear.bias
print(bias)