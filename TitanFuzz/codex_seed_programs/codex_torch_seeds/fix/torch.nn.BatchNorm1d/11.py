'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm1d\ntorch.nn.BatchNorm1d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
data = torch.randn((128, 64))
output = torch.nn.BatchNorm1d(64)(data)
print(output.shape)