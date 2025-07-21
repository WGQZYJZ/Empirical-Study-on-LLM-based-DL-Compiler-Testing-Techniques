'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyBatchNorm1d\ntorch.nn.LazyBatchNorm1d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import numpy as np
print('Task 1: import PyTorch')
print('PyTorch version: {}'.format(torch.__version__))
print('\nTask 2: Generate input data')
input_data = np.random.random((5, 3))
print('input_data: {}'.format(input_data))
print('\nTask 3: Call the API torch.nn.LazyBatchNorm1d')
lazy_batch_norm = nn.LazyBatchNorm1d(3)
print('lazy_batch_norm: {}'.format(lazy_batch_norm))
input_data = torch.tensor(input_data, dtype=torch.float32)
output_data = lazy_batch_norm(input_data)
print('output_data: {}'.format(output_data))