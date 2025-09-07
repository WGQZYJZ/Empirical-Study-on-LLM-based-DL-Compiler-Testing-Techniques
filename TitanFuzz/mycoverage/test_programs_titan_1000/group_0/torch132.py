import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(10, 3)
constraint = torch.distributions.constraints.Constraint()