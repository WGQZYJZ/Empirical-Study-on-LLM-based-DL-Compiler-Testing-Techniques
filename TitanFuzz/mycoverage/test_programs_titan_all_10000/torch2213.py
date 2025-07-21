import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(5, 3)
y = torch.rand(3, 4)
z = torch.matmul(x, y)