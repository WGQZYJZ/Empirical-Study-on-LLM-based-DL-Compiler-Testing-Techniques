'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm1d\ntorch.nn.BatchNorm1d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
from torch.nn import BatchNorm1d
x = torch.randn(100, 2)
bn = BatchNorm1d(2)
bn.train()
y = bn(x)
print(y.mean(0), y.var(0, unbiased=False))
bn.eval()
y = bn(x)
print(y.mean(0), y.var(0, unbiased=False))
bn.train(False)
y = bn(x)
print(y.mean(0), y.var(0, unbiased=False))
bn.eval()
y = bn(x)
print(y.mean(0), y.var(0, unbiased=False))
bn.train(mode=True)
y = bn(x)
print(y.mean(0), y.var(0, unbiased=False))
bn.train(mode=False)
y = bn(x)
print(y.mean(0), y.var(0, unbiased=False))