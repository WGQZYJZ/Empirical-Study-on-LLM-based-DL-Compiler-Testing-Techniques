import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 5, 5)
lrn = torch.nn.LocalResponseNorm(3, alpha=0.0001, beta=0.75, k=1.0)
output = lrn(input)