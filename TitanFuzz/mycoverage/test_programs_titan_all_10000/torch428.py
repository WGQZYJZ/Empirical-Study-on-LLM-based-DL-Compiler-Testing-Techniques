import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 2, 3, 4)
y = torch.frexp(x)