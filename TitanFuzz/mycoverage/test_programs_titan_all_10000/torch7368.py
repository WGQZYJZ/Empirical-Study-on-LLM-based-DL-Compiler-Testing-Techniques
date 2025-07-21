import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, requires_grad=True)
torch.nn.init.constant_(x, 1)
x = torch.randn(3, requires_grad=True)
torch.nn.init.constant_(x, 1)