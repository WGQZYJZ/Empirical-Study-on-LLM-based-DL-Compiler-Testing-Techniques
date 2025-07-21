import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(4, 4)
y = torch.atleast_3d(x)
x = torch.rand(4, 4, 4)
y = torch.atleast_3d(x)