import torch
from torch import nn
from torch.autograd import Variable
x = torch.zeros(2, 1, 2, 1, 2)
y = torch.squeeze(x)
z = torch.squeeze(x, 1)
w = torch.squeeze(x, 0)
u = torch.squeeze(x, 4)