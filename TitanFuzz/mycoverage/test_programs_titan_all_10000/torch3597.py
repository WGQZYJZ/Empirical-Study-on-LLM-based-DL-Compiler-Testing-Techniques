import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(5, requires_grad=True)
b = torch.randn(5, requires_grad=True)
c = torch.randn(5, requires_grad=True)
param_vector = torch.nn.utils.parameters_to_vector([a, b, c])