import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(5, 3)
b = torch.randn(5, 3)
c = torch.randn(5, 3)
d = torch.add(a, b)
e = torch.empty(5, 3)
torch.add(a, b, out=e)
b.add_(a)
a = torch.randn(4, 4)
b