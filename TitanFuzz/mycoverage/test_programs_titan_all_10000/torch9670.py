import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3, 4, 5, 6])
y = torch.tensor([2, 2, 2, 2, 2, 2])
z = torch.floor_divide(x, y)