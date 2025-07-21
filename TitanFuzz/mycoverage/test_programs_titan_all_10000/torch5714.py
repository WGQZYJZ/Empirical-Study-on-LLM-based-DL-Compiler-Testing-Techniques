import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(2, 2)
n = 3
out = torch.linalg.matrix_power(A, n)