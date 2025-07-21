import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3, 4)
y = torch.reshape(x, (3, 8))
z = torch.reshape(x, (1, (- 1)))
w = torch.reshape(x, ((- 1), 1))