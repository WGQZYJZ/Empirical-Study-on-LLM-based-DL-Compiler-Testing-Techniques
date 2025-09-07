import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(100, 5)
(mode, indices) = torch.mode(input, dim=(- 1), keepdim=False)