import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)
y = torch.tensor([[10.0], [20.0]], requires_grad=True)
torch.fmin(x, y)