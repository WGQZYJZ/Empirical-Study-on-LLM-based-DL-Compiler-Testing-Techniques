'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm2d\ntorch.nn.BatchNorm2d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import numpy as np
import torch
import torch.nn as nn
import numpy as np
batch_size = 2
input_channel = 3
height = 4
width = 4
input_data = torch.randn(batch_size, input_channel, height, width)
batch_norm = nn.BatchNorm2d(input_channel)
output_data = batch_norm(input_data)
print(output_data)
print(batch_norm.weight)
print(batch_norm.bias)
print(batch_norm.running_mean)
print(batch_norm.running_var)