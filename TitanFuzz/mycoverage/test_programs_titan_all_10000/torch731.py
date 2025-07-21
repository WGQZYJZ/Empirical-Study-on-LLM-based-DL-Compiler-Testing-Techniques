import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3, dtype=torch.float64, requires_grad=True)
output = torch.cholesky_inverse(input)