import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, requires_grad=True)
target = torch.randn(2, 3)
kldivloss = torch.nn.KLDivLoss()
loss = kldivloss(input, target)