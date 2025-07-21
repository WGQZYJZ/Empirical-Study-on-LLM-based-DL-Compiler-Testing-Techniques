import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(3, 5), requires_grad=True)
target = Variable(torch.randn(3, 5))
loss = torch.nn.KLDivLoss()
output = loss(input, target)