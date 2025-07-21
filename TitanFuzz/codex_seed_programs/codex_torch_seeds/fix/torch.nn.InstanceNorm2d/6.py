'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.InstanceNorm2d\ntorch.nn.InstanceNorm2d(num_features, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)\n'
import torch
from torch.nn import InstanceNorm2d
input_data = torch.randn(1, 3, 5, 5)
instance_norm = InstanceNorm2d(3, momentum=0.1)
output = instance_norm(input_data)
print(output)