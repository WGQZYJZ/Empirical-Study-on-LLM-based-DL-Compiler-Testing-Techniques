import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(2, 3)
y = torch.rand(2, 3)
z = torch.equal(x, y)