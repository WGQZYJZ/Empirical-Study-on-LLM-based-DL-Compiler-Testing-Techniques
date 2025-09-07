import torch
from torch import nn
from torch.autograd import Variable

A = torch.randn(2, 2)
B = torch.randn(2, 2)
X = torch.linalg.solve(A, B)