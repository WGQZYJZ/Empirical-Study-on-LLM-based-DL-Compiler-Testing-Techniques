import torch
from torch import nn
from torch.autograd import Variable
x = torch.Tensor([[1, 2, 3, 4], [4, 3, 2, 1]])
y = torch.nn.LogSoftmax(dim=1)(x)