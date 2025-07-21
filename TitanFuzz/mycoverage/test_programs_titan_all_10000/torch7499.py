import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(1)
y = torch.rand(1)
z = torch.logaddexp(x, y)
z = torch.logaddexp(x, y, out=x)
z = torch.logaddexp(x, y, out=y)