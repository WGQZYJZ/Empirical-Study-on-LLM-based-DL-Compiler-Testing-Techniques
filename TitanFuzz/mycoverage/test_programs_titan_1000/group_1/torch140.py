import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4, 4)
y = torch.randn(4, 4)
z = torch.randn(4, 4)
torch.Tensor.addcdiv_(x, y, z, value=1)