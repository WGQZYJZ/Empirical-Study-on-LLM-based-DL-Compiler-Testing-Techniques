import torch
from torch import nn
from torch.autograd import Variable
x = Variable(torch.Tensor([1, 2, 3, 4, 5, 6]), requires_grad=True)
torch.Tensor.lgamma_(x)