'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyInstanceNorm2d\ntorch.nn.LazyInstanceNorm2d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
input_data = torch.randn(2, 3, 4, 4)
norm = nn.LazyInstanceNorm2d(3)
output = norm(input_data)
print(output)
print(norm.weight)
print(norm.bias)
print(norm.running_mean)
print(norm.running_var)