'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyInstanceNorm1d\ntorch.nn.LazyInstanceNorm1d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
x = torch.randn(1, 2, 3)
print(x)
norm = torch.nn.LazyInstanceNorm1d(2)
y = norm(x)
print(y)