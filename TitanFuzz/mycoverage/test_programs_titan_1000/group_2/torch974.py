import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(10, 10, dtype=torch.float64)
output = torch.matrix_exp(input)