import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(1, 3, 2)
torch.nn.InstanceNorm1d(num_features=3, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)