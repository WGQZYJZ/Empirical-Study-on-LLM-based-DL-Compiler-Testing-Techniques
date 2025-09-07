import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(2, 3)
dim = 1
torch.cumprod(input, dim)