import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 5, 10, 10))
target = Variable(torch.randn(1, 5, 10, 10))
loss = torch.nn.functional.poisson_nll_loss(input, target)