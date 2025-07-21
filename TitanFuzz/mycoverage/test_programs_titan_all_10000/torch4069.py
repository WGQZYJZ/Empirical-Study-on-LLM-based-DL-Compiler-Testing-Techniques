import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(3, 3)
b = torch.matrix_power(a, 2)
c = torch.matrix_power(a, 3)