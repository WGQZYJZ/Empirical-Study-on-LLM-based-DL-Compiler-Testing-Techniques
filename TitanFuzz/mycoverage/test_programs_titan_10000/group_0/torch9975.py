import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(4, 4)
torch.cholesky_inverse(input)
torch.cholesky_inverse(input, upper=True)