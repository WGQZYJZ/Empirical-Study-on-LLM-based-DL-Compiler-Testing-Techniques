'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.InstanceNorm2d\ntorch.nn.InstanceNorm2d(num_features, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)\n'
import torch
from torch import nn
input = torch.randn(4, 3, 6, 6)
instanceNorm2d = nn.InstanceNorm2d(3)
output = instanceNorm2d(input)
print(output)