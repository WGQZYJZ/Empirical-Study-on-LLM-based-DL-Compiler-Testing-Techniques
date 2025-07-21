import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, requires_grad=True)
y = torch.nn.Softplus()(x)
y.backward(torch.tensor([1.0, 1.0, 1.0]))