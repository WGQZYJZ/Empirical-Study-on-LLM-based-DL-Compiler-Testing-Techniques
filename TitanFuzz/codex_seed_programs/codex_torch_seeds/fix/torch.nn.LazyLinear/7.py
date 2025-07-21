'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyLinear\ntorch.nn.LazyLinear(out_features, bias=True, device=None, dtype=None)\n'
import torch
import torch
x = torch.randn(2, 3, requires_grad=True)
print('x: ', x)
linear = torch.nn.LazyLinear(3, 2)
y = linear(x)
print('y: ', y)