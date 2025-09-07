import torch
from torch import nn
from torch.autograd import Variable

A = torch.randn(2, 2)
B = torch.linalg.matrix_power(A, 2)