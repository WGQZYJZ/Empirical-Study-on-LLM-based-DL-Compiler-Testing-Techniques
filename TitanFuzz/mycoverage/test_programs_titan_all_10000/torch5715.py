import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(1, 10)
y = torch.rand(1, 10)
torch.Tensor.igamma_(x, y)