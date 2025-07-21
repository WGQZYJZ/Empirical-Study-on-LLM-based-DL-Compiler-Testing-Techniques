import torch
from torch import nn
from torch.autograd import Variable
x_input = torch.randn(1, 3, 3, 3)
y_output = torch.Tensor.arcsinh_(x_input)