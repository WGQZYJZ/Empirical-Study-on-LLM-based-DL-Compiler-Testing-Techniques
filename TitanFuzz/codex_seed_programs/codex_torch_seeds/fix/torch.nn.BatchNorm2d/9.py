'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm2d\ntorch.nn.BatchNorm2d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_data = torch.randn(20, 5, 3, 3)
bn = nn.BatchNorm2d(5, affine=False)
print('weight:', bn.weight)
print('bias:', bn.bias)
print('running_mean:', bn.running_mean)
print('running_var:', bn.running_var)
output = bn(input_data)