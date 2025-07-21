import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[0, 1, 0], [1, 0, 1]])
y = torch.tensor([[0, 1, 0], [1, 1, 1]])
z = torch.not_equal(x, y)
z = torch.not_equal(x, y, out=x)