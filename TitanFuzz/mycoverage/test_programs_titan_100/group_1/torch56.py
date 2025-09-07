import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 2)
output = torch.matrix_exp(x)