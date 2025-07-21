'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Bilinear\ntorch.nn.Bilinear(in1_features, in2_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
x = torch.randn(1, 4, requires_grad=True)
y = torch.randn(1, 4, requires_grad=True)
bilinear = nn.Bilinear(4, 4, 1)
output = bilinear(x, y)
print(output)
print(output.grad_fn)
print(bilinear.weight)
print(bilinear.bias)