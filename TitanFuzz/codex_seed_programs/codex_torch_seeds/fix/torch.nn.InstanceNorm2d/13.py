'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.InstanceNorm2d\ntorch.nn.InstanceNorm2d(num_features, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)\n'
import torch
from torch.nn import InstanceNorm2d
from torch.nn.functional import instance_norm
input = torch.randn(4, 4, 4, 4)
input_norm = instance_norm(input)
print(input_norm)
input_norm2 = InstanceNorm2d(4)(input)
print(input_norm2)