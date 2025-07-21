'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Linear\ntorch.nn.Linear(in_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
import torch
x = torch.randn(10, 3)
linear_layer = torch.nn.Linear(3, 4)
y = linear_layer(x)
print(y)
print(linear_layer.weight)
print(linear_layer.bias)
linear_layer = torch.nn.Linear(3, 4, bias=False)
print(linear_layer.weight)
print(linear_layer.bias)
linear_layer = torch.nn.Linear(3, 4, bias=False)
print(linear_layer.weight)
print(linear_layer.bias)