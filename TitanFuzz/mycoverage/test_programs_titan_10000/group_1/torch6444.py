import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
torch.set_grad_enabled(mode=False)
z = (x + y)
torch.set_grad_enabled(mode=True)
z = (x + y)
torch.set_grad_enabled(mode=True)
z = (x + y)
torch.set_grad_enabled(mode=False)
z = (x + y)