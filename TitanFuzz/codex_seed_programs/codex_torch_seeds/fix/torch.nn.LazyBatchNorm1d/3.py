'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyBatchNorm1d\ntorch.nn.LazyBatchNorm1d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 2, 3)
lazy_batch_norm = nn.LazyBatchNorm1d(3)
output = lazy_batch_norm(input_data)
print(output)