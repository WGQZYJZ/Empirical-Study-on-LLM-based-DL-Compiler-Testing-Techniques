import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(16, 32, 32)
y = torch.randn(16, 32, 32)
torch.bmm(x, y)