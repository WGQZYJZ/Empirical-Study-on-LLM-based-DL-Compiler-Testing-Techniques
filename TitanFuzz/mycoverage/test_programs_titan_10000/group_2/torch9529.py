import torch
from torch import nn
from torch.autograd import Variable

A = torch.rand(3, 3)
A_power_3 = torch.matrix_power(A, 3)