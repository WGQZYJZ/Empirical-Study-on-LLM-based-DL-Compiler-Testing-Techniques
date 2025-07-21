'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyBatchNorm1d\ntorch.nn.LazyBatchNorm1d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_data = torch.randn(20, 5, 10)
batchnorm_layer = nn.LazyBatchNorm1d(5)
output = batchnorm_layer(input_data)
print(output)