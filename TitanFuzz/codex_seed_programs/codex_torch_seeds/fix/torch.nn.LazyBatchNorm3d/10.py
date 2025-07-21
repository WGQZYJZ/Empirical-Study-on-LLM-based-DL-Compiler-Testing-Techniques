'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyBatchNorm3d\ntorch.nn.LazyBatchNorm3d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
from torch.nn import LazyBatchNorm3d
from torch.autograd import Variable
import numpy as np
input_data = Variable(torch.randn(1, 3, 4, 4, 4))
lazy_batch_norm = LazyBatchNorm3d(3)
output_data = lazy_batch_norm(input_data)
print(output_data)
print(lazy_batch_norm.running_mean)
print(lazy_batch_norm.running_var)
print(lazy_batch_norm.num_batches_tracked)
'\nTask 4: Call the API torch.nn.BatchNorm3d\ntorch.nn.BatchNorm3d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
batch_norm = torch.nn.BatchNorm3d(3)
output_data = batch_norm(input_data)
print(output_data)