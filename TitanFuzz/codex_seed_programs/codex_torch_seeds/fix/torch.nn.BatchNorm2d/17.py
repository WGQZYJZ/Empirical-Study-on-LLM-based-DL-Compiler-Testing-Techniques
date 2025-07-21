'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm2d\ntorch.nn.BatchNorm2d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
from torch.nn import BatchNorm2d
input = torch.randn(20, 16, 35, 45)
bn = BatchNorm2d(16)
output = bn(input)
print(output)