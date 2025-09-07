import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(1, 1)
y = torch.rand(1, 1)
loss = torch.nn.functional.huber_loss(x, y, reduction='mean', delta=1.0)