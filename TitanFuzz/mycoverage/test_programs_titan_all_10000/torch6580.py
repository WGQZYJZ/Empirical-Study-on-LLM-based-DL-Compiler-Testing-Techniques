import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(3, 3)
narrowed = torch.narrow(input, 1, 1, 2)