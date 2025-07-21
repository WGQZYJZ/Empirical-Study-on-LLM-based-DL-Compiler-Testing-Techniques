'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm2d\ntorch.nn.BatchNorm2d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
batch_size = 5
channels = 6
height = 8
width = 10
input = torch.randn(batch_size, channels, height, width)
bn = nn.BatchNorm2d(num_features=channels)
output = bn(input)
print(output)
print(bn.running_mean)
print(bn.running_var)
bn.train()
output = bn(input)
print(bn.running_mean)
print(bn.running_var)
bn.eval()
output = bn(input)
print(output)