import torch
from torch import nn
from torch.autograd import Variable

a = torch.randn(4, 4)
b = torch.randn(4, 4)
c = torch.remainder(a, b)