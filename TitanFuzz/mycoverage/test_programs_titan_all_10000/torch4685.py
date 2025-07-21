import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3, 3)
torch.norm(input, p='fro', dim=None, keepdim=False, out=None, dtype=None)