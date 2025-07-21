import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, requires_grad=True)
torch.Tensor.requires_grad_(x, requires_grad=True)