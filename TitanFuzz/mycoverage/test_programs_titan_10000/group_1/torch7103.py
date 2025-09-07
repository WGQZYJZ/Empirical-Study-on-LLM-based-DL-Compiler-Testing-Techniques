import torch
from torch import nn
from torch.autograd import Variable

A = torch.randn(5, 5)
A_inv = torch.linalg.inv(A)