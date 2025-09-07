import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
y = torch.tensor([1, 1, 1, 1, 1, 1, 0, 0, 0, 0])
result = torch.eq(x, y)