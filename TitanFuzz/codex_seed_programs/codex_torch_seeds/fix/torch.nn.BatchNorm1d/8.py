'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm1d\ntorch.nn.BatchNorm1d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import numpy as np
print('PyTorch version:', torch.__version__)
data = np.random.randn(10, 3)
data = torch.tensor(data, dtype=torch.float32)
print(data)
bn = nn.BatchNorm1d(3)
print(bn)
bn.train()
print(bn.running_mean)
print(bn.running_var)
bn.eval()
print(bn.running_mean)
print(bn.running_var)
bn.train()
out = bn(data)
print(out)
bn.eval()
out = bn(data)
print(out)