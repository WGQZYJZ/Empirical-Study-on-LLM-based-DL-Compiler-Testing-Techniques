import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
input
torch.sum(input, dim=1)
torch.sum(input, dim=1, keepdim=True)
torch.sum(input, dim=0, keepdim=True)
torch.sum(input, dim=(- 1), keepdim=True)