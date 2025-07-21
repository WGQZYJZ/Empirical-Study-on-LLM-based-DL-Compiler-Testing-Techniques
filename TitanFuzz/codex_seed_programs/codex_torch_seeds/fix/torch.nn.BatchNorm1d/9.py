'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm1d\ntorch.nn.BatchNorm1d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
from torch.nn import BatchNorm1d
from torch.nn.parameter import Parameter
import torch
x = torch.randn(10, 3)
bn = BatchNorm1d(3)
bn.weight.data.fill_(1)
bn.bias.data.zero_()
out = bn(x)
print(out)