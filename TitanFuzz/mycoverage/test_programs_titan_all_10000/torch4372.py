import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3)
std = torch.std(input, dim=1)