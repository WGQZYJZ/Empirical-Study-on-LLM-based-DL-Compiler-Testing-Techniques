import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(2, 2)
result = torch.cholesky_inverse(input)