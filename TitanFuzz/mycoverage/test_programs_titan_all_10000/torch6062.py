import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(4, 4)
b = torch.narrow(a, 0, 1, 3)
c = torch.narrow(a, 1, 1, 3)