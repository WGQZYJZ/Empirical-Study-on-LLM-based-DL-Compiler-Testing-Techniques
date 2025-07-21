import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn((2, 3, 4, 5, 6))
torch.nn.LazyBatchNorm3d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)