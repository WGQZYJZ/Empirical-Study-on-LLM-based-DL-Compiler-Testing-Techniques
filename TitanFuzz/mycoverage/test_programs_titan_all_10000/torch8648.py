import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(2, 2)
n = 2
torch.linalg.matrix_power(A, n)