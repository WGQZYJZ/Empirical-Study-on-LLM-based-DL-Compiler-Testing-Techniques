import torch
from torch import nn
from torch.autograd import Variable
n = 2
m = 2
A = torch.randn(n, m)
B = torch.matrix_exp(A)