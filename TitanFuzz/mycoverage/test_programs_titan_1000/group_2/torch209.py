import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, requires_grad=True)
y = torch.randn(3, requires_grad=True)
loss = torch.nn.SoftMarginLoss()
output = loss(x, y)