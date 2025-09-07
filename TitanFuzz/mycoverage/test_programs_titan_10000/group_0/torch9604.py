import torch
from torch import nn
from torch.autograd import Variable

input = torch.rand(1, 1, 5, 5)
target = torch.rand(1, 1, 5, 5)
loss = torch.nn.functional.poisson_nll_loss(input, target)