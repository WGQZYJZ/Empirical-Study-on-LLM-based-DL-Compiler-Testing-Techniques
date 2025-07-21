'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyLinear\ntorch.nn.LazyLinear(out_features, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
x = torch.randn(5, 3)
print(x)
lazy_linear = nn.LazyLinear(3, 5)
print(lazy_linear.weight)
print(lazy_linear.bias)
y = lazy_linear(x)
print(y)
print(lazy_linear.weight)
print(lazy_linear.bias)
print(lazy_linear.weight.shape)
print(lazy_linear.bias.shape)