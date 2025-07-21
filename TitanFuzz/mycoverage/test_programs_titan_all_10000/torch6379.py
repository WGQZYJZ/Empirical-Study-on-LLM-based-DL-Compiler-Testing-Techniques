import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3)
y = torch.randn(2, 1)
z = torch.atleast_3d(x, y)