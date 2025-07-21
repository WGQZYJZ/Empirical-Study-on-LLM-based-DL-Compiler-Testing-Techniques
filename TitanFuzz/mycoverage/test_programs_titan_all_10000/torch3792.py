import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(10, 3)
y = torch.randn(10, 3)
torch.broadcast_shapes(x.shape, y.shape)