'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm1d\ntorch.nn.BatchNorm1d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
input_data = torch.randn(20, 5, 10)
batch_norm = torch.nn.BatchNorm1d(5)
print(batch_norm(input_data))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm2d\ntorch.nn.BatchNorm2d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
input_data = torch.randn(20, 5, 10, 10)
batch_norm = torch.nn.BatchNorm2d(5)