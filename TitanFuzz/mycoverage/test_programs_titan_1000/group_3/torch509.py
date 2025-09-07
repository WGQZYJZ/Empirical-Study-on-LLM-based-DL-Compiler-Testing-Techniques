import torch
from torch import nn
from torch.autograd import Variable
torch.set_printoptions(precision=8)
a = torch.randn(3, 3)
b = torch.randn(3, 1)
c = (a * b)