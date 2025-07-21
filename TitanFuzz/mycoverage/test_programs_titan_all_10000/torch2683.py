import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3)
torch.max(input, dim=0, keepdim=False, out=None)