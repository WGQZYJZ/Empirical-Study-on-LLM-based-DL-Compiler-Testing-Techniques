import torch
from torch import nn
from torch.autograd import Variable
x = torch.Tensor([[1, 2, 3], [4, 5, 6]])
y = torch.Tensor([[1, 2, 3], [4, 5, 6]])
z = torch.ge(x, y)