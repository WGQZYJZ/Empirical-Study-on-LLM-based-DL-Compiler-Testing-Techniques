import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(4, 4)
b = torch.randn(4, 4)
c = torch.lt(a, b)
d = torch.empty(4, 4)
torch.lt(a, b, out=d)
a.lt_(b)
a = torch.randn(4, 4)
b = torch.randn(4, 4)
c = torch.lt(a, b)