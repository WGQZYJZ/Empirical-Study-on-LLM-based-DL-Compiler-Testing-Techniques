'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm2d\ntorch.nn.BatchNorm2d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
from torch.nn import BatchNorm2d
input_data = torch.randn(2, 3, 4, 4)
batch_norm = BatchNorm2d(3)
output = batch_norm(input_data)
print(output)