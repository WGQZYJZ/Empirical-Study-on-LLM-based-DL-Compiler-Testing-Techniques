'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.InstanceNorm2d\ntorch.nn.InstanceNorm2d(num_features, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)\n'
import torch
import numpy as np
from torch.autograd import Variable
x = Variable(torch.randn(1, 3, 3, 3))
import torch
x = Variable(torch.randn(1, 3, 3, 3))
y = torch.nn.InstanceNorm2d(3, affine=False)(x)
print(y)