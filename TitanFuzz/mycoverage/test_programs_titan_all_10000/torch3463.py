import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
other = torch.randn(3, 3)
torch.dist(input, other, p=2)