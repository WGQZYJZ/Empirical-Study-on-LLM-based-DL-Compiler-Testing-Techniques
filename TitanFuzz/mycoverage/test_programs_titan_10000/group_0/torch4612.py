import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(4, 4)
y = torch.randn(4, 4)
z = torch.special.xlogy(x, y)
out = torch.empty(4, 4)
torch.special.xlogy(x, y, out=out)