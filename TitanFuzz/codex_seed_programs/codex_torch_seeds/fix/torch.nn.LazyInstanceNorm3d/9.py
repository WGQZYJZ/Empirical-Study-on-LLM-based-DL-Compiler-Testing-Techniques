'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyInstanceNorm3d\ntorch.nn.LazyInstanceNorm3d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch
input = torch.randn(1, 3, 5, 5, 5)
norm = torch.nn.LazyInstanceNorm3d(3, affine=False)
output = norm(input)
print(output)