import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 3, 5, 5))
norm = torch.nn.LocalResponseNorm(size=2, alpha=0.0001, beta=0.75, k=1.0)
output = norm(input)