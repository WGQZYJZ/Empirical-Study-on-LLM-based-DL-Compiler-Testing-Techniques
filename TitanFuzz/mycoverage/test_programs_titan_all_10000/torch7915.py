import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(2, 3)
b = torch.randn(2)
x = torch.lstsq(b, A)