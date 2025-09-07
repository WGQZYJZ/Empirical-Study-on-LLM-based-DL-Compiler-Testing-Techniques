import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(10)
y = torch.special.i0e(x)
y = torch.special.i0e(x, out=torch.empty(10))