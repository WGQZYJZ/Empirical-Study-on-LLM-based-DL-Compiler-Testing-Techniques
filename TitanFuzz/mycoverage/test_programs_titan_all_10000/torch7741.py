import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(100, 1000)
y = torch.randn(1000, 100)
torch.seed()
out = torch.mm(x, y)
out = torch.randn(1)