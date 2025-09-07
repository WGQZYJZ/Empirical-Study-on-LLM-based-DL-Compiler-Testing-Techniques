import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, requires_grad=True)
y = x.pow(2).sum()
y.backward()
torch.set_flush_denormal(True)
x = torch.randn(1, requires_grad=True)
y = x.pow(2).sum()
y.backward()