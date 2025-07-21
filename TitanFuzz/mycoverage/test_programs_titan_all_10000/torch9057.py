import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(2, 1, 3)
data = torch.randn(2, 1)
data = torch.atleast_3d(data)