'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyInstanceNorm3d\ntorch.nn.LazyInstanceNorm3d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
from torch import nn
from torch.nn import functional as F
from torch.autograd import Variable
import torch
input = torch.randn(2, 3, 5, 5, 5)
input = Variable(input)
m = nn.LazyInstanceNorm3d(3)
output = m(input)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyInstanceNorm3d\ntorch.nn.LazyInstanceNorm3d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
from torch import nn
from torch.nn import functional as F
from torch.autograd import Variable