import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 3)
y = torch.ones(3, 3)
condition = (x > 0.5)
out = torch.where(condition, x, y)
x = torch.rand(3, 3)
y = torch.ones(3, 3)
condition = (x > 0.5)
out = torch.where(condition, x, y)