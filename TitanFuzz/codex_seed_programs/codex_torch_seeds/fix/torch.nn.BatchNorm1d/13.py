'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm1d\ntorch.nn.BatchNorm1d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import numpy as np
import torch
import torch.nn as nn
import numpy as np
x = torch.randn(1, 1, 2, requires_grad=True)
print('x = ', x)
bn = nn.BatchNorm1d(1)
print('bn = ', bn)
print('Weight: ', bn.weight.data)
print('Bias: ', bn.bias.data)
print('Running Mean: ', bn.running_mean)
print('Running Variance: ', bn.running_var)
y = bn(x)
print('y = ', y)
print('Weight: ', bn.weight.data)
print('Bias: ', bn.bias.data)