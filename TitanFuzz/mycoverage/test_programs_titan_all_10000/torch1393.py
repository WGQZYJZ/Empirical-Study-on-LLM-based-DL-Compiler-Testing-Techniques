import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4, 4)
y = torch.expm1(x)
torch.expm1_(x)