import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
torch.atleast_2d(input)
input = torch.randn(2, 3)
torch.atleast_3d(input)