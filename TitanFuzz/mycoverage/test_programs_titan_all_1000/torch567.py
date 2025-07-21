import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4, 4)
y = torch.randn(4, 4)
z = torch.randn(4, 4, requires_grad=True)
torch.addcdiv(x, y, z, value=0.1)