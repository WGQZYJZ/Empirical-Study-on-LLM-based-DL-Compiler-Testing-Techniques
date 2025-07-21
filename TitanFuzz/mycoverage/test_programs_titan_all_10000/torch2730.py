import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(3, 3)
other = torch.rand(3, 3)
torch.special.gammaincc(input, other)