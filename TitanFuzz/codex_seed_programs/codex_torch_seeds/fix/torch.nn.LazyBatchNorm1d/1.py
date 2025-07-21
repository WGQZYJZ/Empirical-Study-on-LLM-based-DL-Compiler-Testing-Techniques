'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyBatchNorm1d\ntorch.nn.LazyBatchNorm1d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import numpy as np
import torch
x = torch.rand(10, 5)
lazy_bn = torch.nn.LazyBatchNorm1d(5)
y = lazy_bn(x)
print(y)
print(y.mean(dim=0))
print(y.var(dim=0))
lazy_bn.eval()
y = lazy_bn(x)
print(y)
print(y.mean(dim=0))
print(y.var(dim=0))
lazy_bn.train()
y = lazy_bn(x)
print(y)
print(y.mean(dim=0))
print(y.var(dim=0))