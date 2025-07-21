import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
torch.matrix_power(input, 2)