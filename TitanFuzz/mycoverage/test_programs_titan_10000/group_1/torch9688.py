import torch
from torch import nn
from torch.autograd import Variable

a = torch.arange(1, 17).view(2, 2, 4)
b = torch.arange(1, 17).view(2, 4, 2)
c = torch.tensordot(a, b, dims=2)