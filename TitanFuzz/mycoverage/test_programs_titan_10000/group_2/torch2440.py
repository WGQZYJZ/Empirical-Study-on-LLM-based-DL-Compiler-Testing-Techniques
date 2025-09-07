import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(3, 3)
mode = torch.mode(input, dim=1)