import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(10, 3)
y = torch.randn(10, 3)
loss = torch.nn.functional.huber_loss(x, y)
loss = torch.nn.functional.huber_loss(x, y, reduction='none')