import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(1, 3, 3)
b = torch.polar(a, a)