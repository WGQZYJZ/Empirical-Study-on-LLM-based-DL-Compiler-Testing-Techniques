import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 10, 10)
target = torch.randn(1, 3, 10, 10)
loss = torch.nn.MSELoss()
loss_value = loss(input, target)