import torch
from torch import nn
from torch.autograd import Variable

x = torch.empty(5, 3)
torch.Tensor.random_(x, from_=0, to=1)
x = torch.empty(5, 3)
torch.Tensor.random_(x, from_=0, to=1)
x = torch.empty(5, 3)