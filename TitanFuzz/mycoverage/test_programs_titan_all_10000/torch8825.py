import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 5)
x = torch.atleast_3d(x)