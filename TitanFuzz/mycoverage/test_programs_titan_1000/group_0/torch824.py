import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3)
target = torch.randn(1, 3)
loss = torch.nn.functional.huber_loss(input, target, reduction='mean', delta=1.0)