import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(2, 3)
y = torch.rand(2, 3)
z = torch.hstack((x, y))
z = torch.zeros(2, 6)
torch.hstack((x, y), out=z)
z = torch.hstack((x, y, x))