import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(1, 3, requires_grad=True)
y = torch.abs(x)