'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyInstanceNorm1d\ntorch.nn.LazyInstanceNorm1d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input_data = torch.randn(1, 3, 5)
layer1 = nn.LazyInstanceNorm1d(3, momentum=0.1)
layer2 = nn.LazyInstanceNorm1d(3, momentum=0.1, affine=False)
output1 = layer1(input_data)
output2 = layer2(input_data)
print('Input data: ', input_data)
print('Output data: ', output1)
print('Output data: ', output2)