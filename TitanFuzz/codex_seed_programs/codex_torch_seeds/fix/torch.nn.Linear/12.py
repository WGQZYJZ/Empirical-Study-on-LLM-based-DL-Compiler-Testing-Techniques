'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Linear\ntorch.nn.Linear(in_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
x = torch.randn(100, 10)
w = torch.randn(10, 5)
b = torch.randn(5)
linear = nn.Linear(10, 5)
y = linear(x)
print('linear.weight: ', linear.weight)
print('linear.bias: ', linear.bias)
print('y: ', y)