import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
torch.argmin(input, dim=None, keepdim=False)