import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3)
y = torch.randn(3, 4)
z = torch.linalg.matmul(x, y)