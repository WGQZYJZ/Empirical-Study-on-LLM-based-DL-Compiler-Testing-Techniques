'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm2d\ntorch.nn.BatchNorm2d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
input = torch.randn(3, 3, 3, 3)
print(input)
batch_norm = nn.BatchNorm2d(3)
print(batch_norm(input))