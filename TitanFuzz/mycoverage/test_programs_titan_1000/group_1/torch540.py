import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4, 4, 4)
lrn = torch.nn.LocalResponseNorm(size=2, alpha=0.0001, beta=0.75, k=1.0)
output = lrn(input)