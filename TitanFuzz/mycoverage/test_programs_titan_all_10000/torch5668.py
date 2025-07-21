import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
b = torch.randn(3, 1)
x = torch.lstsq(b, A)