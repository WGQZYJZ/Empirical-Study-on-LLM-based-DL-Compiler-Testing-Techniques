import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
torch.sum(input, dim=0)
input = torch.randn(4, 4)
torch.sum(input, dim=1)