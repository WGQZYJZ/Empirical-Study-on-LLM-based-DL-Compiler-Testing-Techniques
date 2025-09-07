import torch
from torch import nn
from torch.autograd import Variable

a = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)
c = torch.logaddexp2(a, b)
c.backward()