'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm2d\ntorch.nn.BatchNorm2d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_data = torch.randn(20, 100, 35, 45)
batch_norm_layer = nn.BatchNorm2d(100)
output = batch_norm_layer(input_data)
print(output.size())
print(batch_norm_layer.running_mean)
print(batch_norm_layer.running_var)
batch_norm_layer = nn.BatchNorm2d(100, affine=False)
output = batch_norm_layer(input_data)
print(output.size())
print(batch_norm_layer.running_mean)
print(batch_norm_layer.running_var)