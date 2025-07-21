import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, requires_grad=True)
output = torch.nn.functional.softplus(input)