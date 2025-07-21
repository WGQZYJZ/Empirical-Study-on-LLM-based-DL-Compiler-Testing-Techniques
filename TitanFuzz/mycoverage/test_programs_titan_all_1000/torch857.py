import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 3)
target = torch.randn(1, 3, 3)
loss = torch.nn.functional.l1_loss(input, target)