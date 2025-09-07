import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3, 4])
y = torch.tensor([3, 4, 5, 6])
z = torch.not_equal(x, y)
x = torch.rand(3, 3)
y = torch.not_equal(x, x)