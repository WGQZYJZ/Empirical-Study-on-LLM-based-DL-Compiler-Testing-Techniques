'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm1d\ntorch.nn.BatchNorm1d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
from torch.nn import BatchNorm1d
input_data = torch.randn(100, 128)
batch_norm = BatchNorm1d(128)
output = batch_norm(input_data)
print(output.shape)