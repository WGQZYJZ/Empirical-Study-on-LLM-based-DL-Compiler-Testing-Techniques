import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 1, requires_grad=True)
y = torch.randn(1, 1, requires_grad=True)
loss = torch.nn.MSELoss()