import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 3)
y = torch.rand(3, 3)
res = torch.greater_equal(x, y)