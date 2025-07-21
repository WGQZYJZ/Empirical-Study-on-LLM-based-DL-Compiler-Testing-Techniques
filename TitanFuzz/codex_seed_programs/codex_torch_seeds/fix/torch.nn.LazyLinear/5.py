'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyLinear\ntorch.nn.LazyLinear(out_features, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
x = torch.randn(3, 2)
print('x = ', x)
linear = nn.LazyLinear(2, 3)
print('linear = ', linear)
print('linear.weight = ', linear.weight)
print('linear.bias = ', linear.bias)
y = linear(x)
print('y = ', y)
print('linear.weight.device = ', linear.weight.device)
print('linear.weight.dtype = ', linear.weight.dtype)
print('linear.weight.shape = ', linear.weight.shape)