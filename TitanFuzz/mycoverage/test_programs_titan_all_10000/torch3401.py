import torch
from torch import nn
from torch.autograd import Variable
x = torch.ones(2, 2, requires_grad=True)
torch.nn.init.constant_(x, val=2.0)
x = torch.ones(2, 2, requires_grad=True)
torch.nn.init.eye_(x)