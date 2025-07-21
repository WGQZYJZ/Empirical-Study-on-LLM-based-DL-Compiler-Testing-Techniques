import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(2, 3, 4)
torch.deg2rad(input, out=None)
input = torch.rand(2, 3, 4)
other = torch.rand(2, 3, 4)
torch.dist(input, other, p=2)