import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 2, 3, 4)
y = torch.randn_like(x)
z = torch.rand(2, 3)
a = torch.rand_like(z)