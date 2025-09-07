import torch
from torch import nn
from torch.autograd import Variable

a = torch.randn(4, 4)
b = torch.randn(4, 4)
c = torch.sub(a, b)
a = torch.randn(4, 4)
b = torch.randn(4, 4)
a.sub_(b)
a = torch.randn(4, 4)
b = torch.randn(4, 4)
c = torch.mul(a, b)
a = torch.randn(4, 4)
b = torch.randn(4, 4)
a.mul_(b)