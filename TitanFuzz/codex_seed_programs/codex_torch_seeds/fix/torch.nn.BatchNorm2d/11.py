'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm2d\ntorch.nn.BatchNorm2d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input_data = torch.randn(20, 5, 35, 45)
bn = nn.BatchNorm2d(5)
output_data = bn(input_data)
print(output_data.size())