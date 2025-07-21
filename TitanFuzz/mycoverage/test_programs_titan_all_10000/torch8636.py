import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1))
target = Variable(torch.randn(1, 1))
loss = torch.nn.functional.mse_loss(input, target)