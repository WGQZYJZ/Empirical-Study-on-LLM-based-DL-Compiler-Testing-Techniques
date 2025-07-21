'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm2d\ntorch.nn.BatchNorm2d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input = torch.randn(20, 100, 35, 45)
m = nn.BatchNorm2d(100)
output = m(input)
print(output.shape)
print(m.weight)
print(m.bias)
print(m.running_mean)
print(m.running_var)
print(m.training)
m.eval()
print(m.training)