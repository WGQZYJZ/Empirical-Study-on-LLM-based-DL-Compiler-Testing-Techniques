import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.randn(1, 1, 3, 3))
y = Variable(torch.randn(1, 1, 3, 3))
loss = torch.nn.functional.l1_loss(x, y)