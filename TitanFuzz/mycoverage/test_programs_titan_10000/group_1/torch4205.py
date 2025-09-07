import torch
from torch import nn
from torch.autograd import Variable

a = torch.randn(2, 3, 4)
b = torch.randn(2, 4, 5)
c = torch.bmm(a, b)