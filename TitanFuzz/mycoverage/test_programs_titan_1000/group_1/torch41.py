import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4, 3)
y = torch.randn(3, 5)
z = torch.matmul(x, y)