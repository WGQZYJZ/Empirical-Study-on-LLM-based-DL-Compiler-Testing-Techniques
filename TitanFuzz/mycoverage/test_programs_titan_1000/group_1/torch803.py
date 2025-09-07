import torch
from torch import nn
from torch.autograd import Variable
A = torch.rand(5, 5)
n = 3
torch.linalg.matrix_power(A, n)